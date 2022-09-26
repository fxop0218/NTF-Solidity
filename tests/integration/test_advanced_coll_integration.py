import pytest

from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import get_account, get_contract, LOCAL_BLOCKCHAIN_ENV
from brownie import network, config, AdvancedCollectible

def test_can_create_advanced_collectible():
    # Deploy the contract
    # Create NFT
    