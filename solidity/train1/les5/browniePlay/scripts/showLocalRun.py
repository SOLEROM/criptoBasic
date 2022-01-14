from brownie import accounts
import os

def main():
    print("localRun")
    account = accounts[0]
    print(account)

    print("cliAccounts")
    account = accounts.load("play1account") 
    print(account)

    print("envAccounts")
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)