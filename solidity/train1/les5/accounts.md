

# (1) use local accounts

```
browniePlay/scripts/showLocalRun.py
====================================
from brownie import accounts

def main():
    print("localRun")
    account = accounts[0]
    print(account)



>brownie run scripts/showLocalRun.py
====================================
Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

Running 'scripts/showLocalRun.py::main'...
localRun
0x66aB6D9362d4F35596279692F0251Db635165871

```

# (2) use cli inner accounts

cli add 

```
> brownie accounts new "play1account"

Brownie v1.17.2 - Python development framework for Ethereum

Enter the private key you wish to add: 0xffdd7a010ab8c089d95a9c2ff24e75b21744b5db26c3cd66d14f8e91c46afcc4
Enter the password to encrypt this account with: 
SUCCESS: A new account '0xdbB4A708755dfD59f9c4b100B2BE23a6d2EB7D57' has been generated with the id 'play1account'
```


cli list

```
> brownie accounts list
Brownie v1.17.2 - Python development framework for Ethereum

Found 1 account:
 └─play1account: 0xdbB4A708755dfD59f9c4b100B2BE23a6d2EB7D57
```


script 

```
from brownie import accounts

def main():
    print("cliAccounts")
    account = accounts.load("play1account")
    print(account)
```

run

```
cliAccounts
Enter password for "play1account": 
0xdbB4A708755dfD59f9c4b100B2BE23a6d2EB7D57
```

# (3) form env file due to yaml rule


```
<brownieInitFolder>/brownie-config.yaml
========================================
dotenv: .env
```

```
.env
=====
PRIVATE_KEY="0xffdd7a010ab8c089d95a9c2ff24e75b21744b5db26c3cd66d14f8e91c46afcc4"
```


```
scripts/

from brownie import accounts
import os

def main():
    print("envAccounts")
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)

    ```

run

```
Running 'scripts/showLocalRun.py::main'...
envAccounts
0xdbB4A708755dfD59f9c4b100B2BE23a6d2EB7D57
```


# (4) form env file due to yaml rule without os



```
<brownieInitFolder>/brownie-config.yaml
========================================
dotenv: .env
wallets:
  from_key: ${PRIVATE_KEY}
```

```
.env
=====
PRIVATE_KEY="0xffdd7a010ab8c089d95a9c2ff24e75b21744b5db26c3cd66d14f8e91c46afcc4"
```


```
scripts/

from brownie import accounts, config
import os

def main():
    print("envAccounts")
    account = accounts.add(config["wallets"]["from_key"])

    print(account)

    ```
