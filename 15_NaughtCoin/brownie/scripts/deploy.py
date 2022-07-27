from brownie import NaughtCoin
from .helpful_scripts import get_account


def deploy_naughtcoin():
    """
    Deploy the naughtcoin contract
    brownie run scripts/deploy.py --network ganache-local
    """
    account = get_account()
    print(f"Using the account {account}")
    naughtcoin = NaughtCoin.deploy(
        account.address,
        {"from": account},
        publish_source=False,
    )
    print(f"Contract NaughtCoin deployed to {naughtcoin.address} and player: {naughtcoin.player()}")
    return naughtcoin


def main():
    pass
    # deploy_naughtcoin()
    # deploy_nauthcoinattack()