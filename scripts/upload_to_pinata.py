import os
from pathlib import Path
import requests
import json
import xmltodict

PINATA_BASE_URL = "https://app.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {"pinata_api_key" : os.getenv("PINATA_APY_KEY"), "pinata_secret_api_key" : os.getenv("PINATA_API_SECRET")}


def main():
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.request(
            "POST",
            PINATA_BASE_URL + endpoint,
            files ={"file" : (filename, image_binary)},
            headers=headers
        )
        print(response)