from random import sample
from scripts.helpful_scripts import get_account, OPENSEA_MAIN_PAGE_URL, get_contract
from brownie import SimpleCollectable
from web3 import Web3

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

def deploy_and_create():
    account = get_account()
    simple_collectable = SimpleCollectable.deploy({"from" : account})
    transaction = simple_collectable.createCollectable(sample_token_uri, {"from" : account})
    transaction.wait(1)
    print(f"You can view your NFT at {OPENSEA_MAIN_PAGE_URL.format(simple_collectable.address, simple_collectable.tokenCounter() - 1)}")
    return simple_collectable

def main():
    deploy_and_create()


def fund_with_link(contract_address, account = None, link_token = None, amount=Web3.toWei(1, "ether")): 
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")
    funding_transaction = link_token.transfer(contract_address, amount, {"from" : account})
    funding_transaction.wait(1)
    print(f"Funded in {contract_address}")
    return funding_transaction


