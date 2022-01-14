# deploy


* import the code using from brownie
* deploy in one line instead of web3 tx-sign...


```python
from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})


def main():
    deploy_simple_storage()
```

```

Running 'scripts/deploy.py::main'...
Transaction sent: 0x3e3ec28da4ee9a7b53bc03c87b0ffb2ed541c434e63125333094bb372eb3844d
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  SimpleStorage.constructor confirmed   Block: 1   Gas used: 335404 (2.80%)
  SimpleStorage deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87


```


## update value in contact

```
from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # update value in contract
    transaction = simple_storage.store(15, {"from": account})
    # wait for  block
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
```


```
Transaction sent: 0xbd20897ba62d3fa6ecbafeef2f955917ae6894dd6371d923ad7cd6be5ece0699
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
  SimpleStorage.store confirmed   Block: 2   Gas used: 41416 (0.35%)

  SimpleStorage.store confirmed   Block: 2   Gas used: 41416 (0.35%)

15
```