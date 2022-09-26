import os
import requests
import collections
from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.metadata_tmp import metadata_template
from pathlib import Path


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You hace crated {number_of_advanced_collectibles} collectibles")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        collectible_metadata = metadata_template
        print(metadata_file_name)
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} exists, delete to overwrite")
        else:
            print(f"{metadata_file_name} created")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An {breed} pup"
            img_path = "./img/" + breed.lower().replace("_","-") + ".png"
            
def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # Upload the stuf More info: https://docs.ipfs.tech/install/command-line/#official-distributions
        # ipfs daemon
        ipfs_url = os.environ.get("IPFS_URL")
        end_point = "/api/v0/add"
        response = requests.post(ipfs_url + end_point, files={"file":image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/X-PUG.png" to "X-PUG.png" X ==> number
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        return image_uri