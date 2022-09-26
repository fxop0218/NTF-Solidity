from scripts.helpful_scripts import get_account, OPENSEA_MAIN_PAGE_URL, get_contract
from brownie import AdvancedCollectible, network, config

from scripts.simple_collectible.dpeloy_and_create import fund_with_link

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
def deploy_and_create():
    account = get_account()
    advanced_collectable = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectable.address)
    creating_tx = advanced_collectable.createCollectible({"from" : account})
    creating_tx.wait(1)
    print(f"New token has been created")
    return advanced_collectable, creating_tx

def main():
    deploy_and_create()
