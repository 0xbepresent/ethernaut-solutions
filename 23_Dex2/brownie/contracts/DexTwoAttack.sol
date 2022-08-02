// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/token/ERC20/ERC20.sol";

contract DexTwoAttack is ERC20 {
    constructor(uint256 initialSupply) ERC20("Bepresent", "BT") public {
        _mint(msg.sender, initialSupply);
    }
}
