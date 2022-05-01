from brownie import accounts, config, NumberStorage, network

def get_account():
	if (network.show_active() == "development"):
		print("This is a dev-NET !")
		return accounts[0]
	else:
		print("This is a testnet..")
		return accounts.add(config["wallets"]["from_key"])


def deploy_number_storage():
	account = get_account()
	number_storage = NumberStorage.deploy({"from":account})

	# store:
	txn = number_storage.store(55, {"from":account})
	txn.wait(1)

	# retrieve:
	retrieved = number_storage.retrieve()
	print(retrieved)

def main():
	deploy_number_storage()