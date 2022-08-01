from brownie import Shop, BuyerAttack
from scripts.helpful_scripts import get_account


def test_shop():
    account = get_account()
    # Deploy shop
    shop = Shop.deploy({"from": account})

    # Deploy attack shop. Changing the price, that's possible
    # because the price function of the Buyer interface is not
    # implemented
    buyerattack = BuyerAttack.deploy({"from": account})
    assert shop.isSold() == False

    print(f"Shop address: {shop.address} Buyer attacker address: {buyerattack.address}")
    buyerattack.attack(shop.address, {"from": account})

    assert shop.price() == 0
    assert shop.isSold() == True
