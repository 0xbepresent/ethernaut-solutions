from brownie import GatekeeperTwo, GatekeeperTwoAttack
from .helpful_scripts import get_account


def deploy_gatekeepertwo():
    """
    Deploy the gatekeepertwo contract
    brownie run scripts/deploy.py --network ganache-local
    """
    account = get_account()
    # Verify the code on etherscan
    print(f"Using the account {account}")
    gatekeepertwo = GatekeeperTwo.deploy(
        {"from": account},
        publish_source=False,
    )
    print(f"Contract GatekeeperTwo deployed to {gatekeepertwo.address}")

    # Verify the code on etherscan
    print(f"Using the account {account}")
    gatekeepertwoattack = GatekeeperTwoAttack.deploy(
        gatekeepertwo.address,
        {"from": account},
        publish_source=False,
    )
    print(f"Contract GatekeeperTwoAttack deployed to {gatekeepertwoattack.address}")
    return gatekeepertwo


def main():
    deploy_gatekeepertwo()
