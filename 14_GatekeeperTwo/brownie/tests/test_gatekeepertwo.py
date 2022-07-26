from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_gatekeepertwo


def test_gatetwo():
    account = get_account()
    print(f"Using the account {account}")

    # gatekeepertwo
    gatekeepertwo = deploy_gatekeepertwo()
    print(f"Contract GateKeeperTwo deployed {gatekeepertwo}")
    print(f"Entrant: {gatekeepertwo.entrant()}")

    # Assert the entrant is filled with our account address
    assert gatekeepertwo.entrant() == account.address
