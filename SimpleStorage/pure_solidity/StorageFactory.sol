// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

import "./SimpleStorage.sol";

contract StorageFactory is SimpleStorage{
	
	// Create as much as storage contracts needed
	SimpleStorage[] public simpleStorageArray;
	uint256 numberOfContracts;

	function createSimpleStorageContract() public {
		SimpleStorage simplestorage = new SimpleStorage();
		simpleStorageArray.push(simplestorage);
	}
	
	function getNbrOfContracts() public view returns(uint256){
		return simpleStorageArray.length;
	}
	// Call the basic functionnality
	function sfAddPerson(uint256 _simpleStorageIndex, string memory _name, uint256 _age) public {
		SimpleStorage simplestorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
		simplestorage.addPerson(_name, _age);
	}
	
	function sfGetPerson(uint256 _SimpleStorageIndex, string memory _name) public view returns(uint256) {
		SimpleStorage simplestorage = SimpleStorage(address(simpleStorageArray[_SimpleStorageIndex]));
		simplestorage.findAge(_name);
	}

}
