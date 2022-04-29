# Simple Storage application.

### Simple example 1: Simple Storage example

- SimpleStorage.sol: Store an undefinite number of people in an array and retrieve the age of each one by name when needed. We need to: 
	- Define an array to store names and ages.
	- Define a function to store new people.
	- Define a mapping to map names to ages.
	- Define a function to retireve a person's age.
[OBJ: Build a simple and basic contract and use the basic syntax of solidity]

### Simple Example 2: Storage Factory

- StorageFactory.sol: Use the functions of SimpleStorage from another contract. We need to:
	- Import the SimpleStorage contract.
	- Define a new contract that points to the SimpleStorage by the keywoard "is".
	- Define an array of contracts to deploy and interact with as much contracts as we want through their index in the defined array.
	- Define functions that call the function of SimpleStorage and define the smart contract to be used from the array at each function call.
	
[OBJ: call a contract from a second contract]

### Simple Example 3: FundMe contract

- FundMe.sol: Use the chainlink DataFeeds 




[OBJ: Working with Chainlink DataFeeds for price conversions]

