from brownie import accounts, config, SimpleStorage
import os

def deploy_dotenv():
	account = accounts.add(os.getenv("PRIVATE_KEY"))
	simple_storage = SimpleStorage.deploy({"from":account})
	print(simple_storage)


def deploy_yaml():
	account = accounts.add(config["wallets"]["from_key"])
	simple_storage = SimpleStorage.deploy({"from":account})
	print(simple_storage)

def main():
	
	print("\nDeploy with .env\n")
	deploy_dotenv()

	print("\nDeploy with yaml\n")
	deploy_yaml()