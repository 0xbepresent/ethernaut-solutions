// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/math/SafeMath.sol";

contract GatekeeperOne {

  using SafeMath for uint256;
  address public entrant;
  uint256 public gasto;
  uint256 public modgas;

  modifier gateOne() {
    require(msg.sender != tx.origin, "Gate ONE ERROR");
    _;
  }

  modifier gateTwo() {
    require(gasleft().mod(8191) == 0, "Gate TWO ERROR");
    _;
  }

  modifier gateThree(bytes8 _gateKey) {
      require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
      require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
      require(uint32(uint64(_gateKey)) == uint16(tx.origin), "GatekeeperOne: invalid gateThree part three");
    _;
  }

  function enter(bytes8 _gateKey) public returns (uint256) {
    gasto = gasleft();
    modgas = gasto.mod(8191);
    entrant = tx.origin;
    return 1337;
  }
}
