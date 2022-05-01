// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
	
	struct People {
		string name;
		uint256 age;
	}
	
	People[] public people;
	mapping(string => uint256) nameToAge;
	
	function addPerson(string memory _name, uint256 _age) public {
		people.push(People(_name, _age));
		nameToAge[_name] = _age;
	}
	
	function findAge(string memory _name) public view returns(uint256) {
		return nameToAge[_name];
	}

}
