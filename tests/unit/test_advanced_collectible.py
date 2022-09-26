from typing_extensions import assert_type
from brownie import network, AdvancedCollectible
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV, get_account, get_contract

def test_can_creadte_adv_coll():
    # Deploy the contract 
    # Generate NFT
    # Get random breed
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only local test")
    advanced_collectible, creation_transaction = deploy_and_create()
    requestId = creation_transaction.events["requestedCollectable"]["requestId"]
    random_number = 127
    get_contract("vrf_coordinator").callBackWithRandomness(requestId,random_number , advanced_collectible.address, {"from": get_account()})
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3