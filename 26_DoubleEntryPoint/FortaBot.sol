// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./CryptoVault.sol";


contract FortaBot is IDetectionBot{

    address constant VAULT = 0x1a1F0F09d4818F15773922a16618B76fa630D923;

    function handleTransaction(address user, bytes calldata msgData) external override{
    (,,address origSender) = abi.decode(msgData[4:], (address, uint256, address));
        if (origSender == VAULT) {
            IForta(msg.sender).raiseAlert(user);
        }
    }
}