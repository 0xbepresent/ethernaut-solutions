import os

from brownie import config, GatekeeperOne, GatekeeperOneAttack, network

from .helpful_scripts import get_account


def deploy_gatekeeperone():
    account = get_account()
    # Verify the code on etherscan
    print(f"Using the account {account}")
    gatekeeperone = GatekeeperOne.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {gatekeeperone.address}")
    return gatekeeperone


def deploy_gatekeeperoneattack():
    account = get_account()
    # Verify the code on etherscan
    print(f"Using the account {account}")
    gatekeeperoneattack = GatekeeperOneAttack.deploy(
        {"from": account},
        publish_source=False,
    )
    print(f"Contract deployed to {gatekeeperoneattack.address}")
    return gatekeeperoneattack


def main():
    # deploy_gatekeeperone()
    deploy_gatekeeperoneattack()
