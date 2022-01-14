# interact with contract

* (1) the deployed contracts are in build deployments folder ; it is a list ; -1 get the last one
* (2) brownie knows about the abi and code so can interact directly

```
from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]  //(1)
    print(simple_storage.retrieve())    //(2)


def main():
    read_contract()


```