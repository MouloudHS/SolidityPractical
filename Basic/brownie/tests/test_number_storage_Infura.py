from brownie import accounts, config, NumberStorage, network

def get_account():
	if (network.show_active() == "development"):
		print("Developpment network ON !")
		return accounts[0]
	else:
		print("This is a testnet")
		return accounts.add(config["wallets"]["from_key"])

def test_deploy_number_storage():

	# Arrange: 
	account = get_account()

	# Act:
	number_storage = NumberStorage.deploy({"from":account})
	number = number_storage.retrieve()
	expected_number = 0

	# Assert:
	assert expected_number == number

def test_update_number_storage():

	# Arrange: 
	account = get_account()

	# Act:
	number_storage = NumberStorage.deploy({"from":account})
	
	expectation = 55
	txn = number_storage.store(expectation, {"from":account})
	txn.wait(1)
	retrieved = number_storage.retrieve()

	# Assert:
	assert expectation == retrieved

