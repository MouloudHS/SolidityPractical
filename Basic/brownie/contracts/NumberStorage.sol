pragma solidity ^0.6.0;

contract NumberStorage {

	uint256 number;

	function store(uint256 _number) public {
		number = _number;
	}

	function retrieve() public view returns(uint256) {
		return number;
	}
}