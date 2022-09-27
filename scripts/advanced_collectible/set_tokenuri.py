from brownie import network, AdvancedCollectible, config
from scripts.helpful_scripts import OPENSEA_MAIN_PAGE_URL, get_account, get_breed

dog_metadata_d = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}
NETWORKS = "networks"

def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectible = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectible} tokenIds")
    for token_id in range(number_of_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, dog_metadata_d)

def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    transaction = nft_contract.setTokenUri(token_id, tokenURI, {"from" : account})
    transaction.wait(1)
    print(f"You can view your nft at {OPENSEA_MAIN_PAGE_URL.format(nft_contract.address, token_id)}")
