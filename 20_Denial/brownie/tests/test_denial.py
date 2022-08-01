from brownie import Denial, DenialAttack

from scripts.helpful_scripts import get_account


def test_denial():
    account = get_account()

    # Deploy Denial contract
    denial = Denial.deploy({"from": account})
    account.transfer(denial.address, 100)

    assert denial.balance() == 100

    # Deploy DenialAttack contract
    denialattack = DenialAttack.deploy({"from": account})

    # Set attacker partner
    denial.setWithdrawPartner(denialattack.address, {"from": account})

    # Call the withdraw function
    denial.withdraw({"from": account})

    # Check funds to 0
    assert denial.balance() == 0
