// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

interface Building {
  function isLastFloor(uint) external returns (bool);
}


contract Elevator {
  bool public top;
  uint public floor;

  function goTo(uint _floor) public {
    // Se construye la interfaz building pero con base al msg.sender
    // esto hace que la variable building busque la funcion isLastFloor
    // pero desde el contrato que fue llamado, es decir, desde el contrato
    // msg.sender
    Building building = Building(msg.sender);

    if (! building.isLastFloor(_floor)) {
      floor = _floor;
      top = building.isLastFloor(floor);
    }
  }
}
