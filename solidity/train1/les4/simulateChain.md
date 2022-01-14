# simulate chain for local testing

## ganache

https://trufflesuite.com/ganache/

```text
Quickly fire up a personal Ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates.
```

## (A) connecting to appimage elf 

```
from web3 import Web3

# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
chain_id = 1337
my_address = "0xdbB4A708755dfD59f9c4b100B2BE23a6d2EB7D57"
private_key = "0xffdd7a010ab8c089d95a9c2ff24e75b21744b5db26c3cd66d14f8e91c46afcc4"


```

## (B) cli way

```
> npm install -g ganache-cli
> ganache-cli --version
Ganache CLI v6.12.2 (ganache-core: 2.13.2)
```


```
>ganache-cli          
...
.....

Listening on 127.0.0.1:8545

```
