import pytest
import time

from brownie import network, AdvancedCollectible
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV

def test_can_creadte_adv_coll_integration():
    # Deploy the contract 
    # Generate NFT
    # Get random breed
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only integration test")
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
