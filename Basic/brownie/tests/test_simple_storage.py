from brownie import accounts, SimpleStorage, config

def test_simple_storage():

	# Arrange:
	account = accounts[0]

	# Act:
	simple_storage = SimpleStorage.deploy({"from":account})
	name, age = "Mouloud", 25
	simple_storage.addPerson(name, age, {"from":account})
	expected_age = simple_storage.findAge(name)

	# Assert
	assert expected_age == age