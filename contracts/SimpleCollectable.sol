//SPDX-License-Identifier: MIT
// More information ERC721 : https://eips.ethereum.org/EIPS/eip-721
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract SimpleCollectable is ERC721, ERC721URIStorage {
    uint256 public tokenCounter;
    constructor() ERC721("Dog_nft", "DOG") {
        tokenCounter = 0;
    }

    function createCollectable(string memory _tokenURI) public returns(uint256) {
        uint256 newTokenId = tokenCounter;
        // Use _safeMint
        _safeMint(msg.sender, newTokenId); // To, tokenId
        _setTokenURI(newTokenId, _tokenURI);
        tokenCounter = tokenCounter + 1;
        return newTokenId;
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