//SPDX-License-Identifier: MIT
// More information ERC721 : https://eips.ethereum.org/EIPS/eip-721
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, ERC721URIStorage, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum Breed{PUG, SHIBA_INU, ST_NERNARD}
    mapping(uint256 => Breed) tokenIdToBreed;
    mapping(bytes32 => address) requestIdToSender;
    event requestedCollectable (bytes32 indexed requestId, address requester);
    event breedAssigned(uint256 indexed tokenId, Breed breed);

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee)
    VRFConsumerBase(_vrfCoordinator, _linkToken)
    ERC721("Dogs", "DGS") {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee; 
    }

    function createCollectable(string memory _tokenURI) public returns(bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectable(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        Breed breed = Breed(randomNumber % 3);
        uint256 newTokenId = tokenCounter;
        tokenIdToBreed[newTokenId] = breed;
        emit breedAssigned(newTokenId, breed);
        address owner = requestIdToSender[requestId];
        // Use _safeMint
        _safeMint(owner, newTokenId);
        tokenCounter = tokenCounter + 1; 
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: Caller is not the owner");
        _setTokenURI(tokenId, _tokenURI);
    }

    // Needed by ERC721URIStorage
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}