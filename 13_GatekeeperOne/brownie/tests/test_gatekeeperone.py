from brownie import accounts, network, exceptions
from brownie import exceptions, Contract
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_gatekeeperone, deploy_gatekeeperoneattack

import pytest


def test_gatetwo():
    account = get_account()
    print(f"Using the account {account}")

    # GateKeeperOne
    gatekeeperone = deploy_gatekeeperone()
    print(f"Contract GateKeeperOne deployed {gatekeeperone}")

    # GateKeeperAttack
    gatekeeperoneattack = deploy_gatekeeperoneattack()
    print(f"Contract GateKeeperOneAttack deployed {gatekeeperoneattack}")

    # Test de tx.origin != msg.sender
    # with pytest.raises(exceptions.VirtualMachineError):
    #     gatekeeperone.enter("121212")

    # with pytest.raises(ValueError):
    r = gatekeeperoneattack.attack(gatekeeperone.address)
    print(f"Event : {r.events}")

    assert gatekeeperone.gasto() != 0
    assert gatekeeperone.gasto() == 0
