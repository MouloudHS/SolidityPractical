from brownie import accounts, StorageFactory
import time


def deploy_storage_factory():
	account = accounts[0]
	storage_factory = StorageFactory.deploy({"from":account})
	
	time.sleep(2)
	print("Creating 5 contracts...\n")
	# Creating 5 contracts
	for i in range(5):
		Contract = storage_factory.createSimpleStorageContract()

	# Printing the number of contracts
	NbrOfContracts = storage_factory.getNbrOfContracts()
	print("Number of deployed contracts from Storage Factory is: ", NbrOfContracts)
	

	time.sleep(2)
	print("Adding person...\n")
	index, name, age = 0, "Mouloud", 25
	txn = storage_factory.sfAddPerson(index, name, age, {"from":account})
	txn.wait(1)
	
	print("Getting person's age...\n")	
	nameToAge = storage_factory.sfGetPerson(index, name)
	print("Age = ", nameToAge)
	
def main():
	print("Deploying....\n")
	deploy_storage_factory()
	
	
	
	
	
	
	
