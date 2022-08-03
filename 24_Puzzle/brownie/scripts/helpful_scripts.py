from brownie import accounts, config, network
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        account = accounts[0]
    else:
        # Infura
        account = accounts.add(config["wallets"]["from_key"])
    return account
