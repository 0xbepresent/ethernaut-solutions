from brownie import PuzzleWallet, PuzzleProxy, accounts
from web3 import Web3

from scripts.helpful_scripts import get_account


def test_puzzle():
    """
    Steps:
        - Propose a new admin in proxy contract.
        - Assert PuzzleWallet the new owner is de proposed user.
        - Call multipletimes the multicall function.
        - Call execute function in order to transfer balance to another user.
        - Balance is 0
        - SetMaxBalance the new admin
        - Proxy has a new admin
    """
    account = get_account()
    # Deploy the puzzlewallet
    pw = PuzzleWallet.deploy({"from": account})
    pw.init(5000000000000000, {"from": account})
    assert pw.owner() == account.address

    pp = PuzzleProxy.deploy(account.address, pw.address, bytes(0x00), {"from": account})

    # Propose a new admin in proxy contract and assert the owner
    pp.proposeNewAdmin(accounts[0], {"from": account})
    assert pw.owner() == accounts[0].address

    # Add to the whitelist our user and assert in whitelisted array
    pw.addToWhitelist(accounts[0], {"from": accounts[0]})
    assert pw.whitelisted(accounts[0]) is True

    # Call multicall multiple times
    # Method id for deposit() function
    deposit_keccak = Web3.keccak(text="deposit()")[:4].hex()
    multicall_calldata = pw.multicall.encode_input([deposit_keccak])
    print(f"The multicalldata: {multicall_calldata}")
    data = [deposit_keccak, multicall_calldata]
    pw.multicall(data, {"from": accounts[0], "value": Web3.toWei(0.001, "ether")})
    assert pw.balance() == Web3.toWei(0.001, "ether")
    assert pw.balances(accounts[0].address) == Web3.toWei(0.002, "ether")

    # Call execute to remove all balance
    pw.execute(
        accounts[0].address,
        Web3.toWei(0.001, "ether"),
        bytes(0x00),
        {"from": accounts[0]},
    )
    assert pw.balance() == 0

    # Set new admin
    assert pp.admin() == account.address
    pw.setMaxBalance(accounts[0].address, {"from": accounts[0]})
    assert pp.admin() == accounts[0].address
