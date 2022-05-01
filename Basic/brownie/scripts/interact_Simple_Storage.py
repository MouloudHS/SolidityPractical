from brownie import accounts, SimpleStorage


def deploy_simple_storage():

	# Get an account from ganache-cli 
	account = accounts[0]
	
	# Deployement
	print("Deployement..")
	simple_storage = SimpleStorage.deploy({"from": account})
	
	# AddPerson function:
	print("\nAdd a person to People list...")
	name, age = "Mouloud", 25
	txn = simple_storage.addPerson(name, age, {"from":account})
	txn.wait(1)
	
	# Find Age of corresponding person
	print("\n Find the age of a person from the list from it's name...")
	age_from_name = simple_storage.findAge(name)
	print(f"\nThe age of {name} is {age_from_name}")

def main():
	deploy_simple_storage()