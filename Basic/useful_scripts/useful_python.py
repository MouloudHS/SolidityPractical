from brownie import config, accounts, network

def get_account():
	if (network.show_active() == "development"):
		print("Developpment network ON !")
		return accounts[0]
	else:
		print("This is a testnet")
		return accounts.add(config["wallets"]["from_key"])
