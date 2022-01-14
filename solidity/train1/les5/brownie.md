# Brownie 

##  install

```
https://eth-brownie.readthedocs.io/en/stable/install.html
==========================================================
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install eth-brownie

> brownie

Brownie v1.17.2 - Python development framework for Ethereum

```

## cmds

```
Brownie v1.17.2 - Python development framework for Ethereum

Usage:  brownie <command> [<args>...] [options <args>]

Commands:
  init               Initialize a new brownie project
  bake               Initialize from a brownie-mix template
  pm                 Install and manage external packages
  compile            Compile the contract source files
  console            Load the console
  test               Run test cases in the tests/ folder
  run                Run a script in the scripts/ folder
  accounts           Manage local accounts
  networks           Manage network settings
  gui                Load the GUI to view opcodes and test coverage
  analyze            Find security vulnerabilities using the MythX API


```

## init

```
brownie init
Brownie v1.17.2 - Python development framework for Ethereum

SUCCESS: A new Brownie project has been initialized at /...../brownieInit

.
├── build
│   ├── contracts
│   ├── deployments
│   └── interfaces
├── contracts
├── interfaces
├── reports
├── scripts
└── tests

```


## compile

```
> brownie compile

.
├── build
│   ├── contracts
│   │   └── SimpleStorage.json
│   ├── deployments
│   └── interfaces
├── contracts
│   └── SimpleStorage.sol
├── interfaces
├── reports
├── scripts
└── tests
```

## run

* add scripts to script folder and use ``` brownie run scripts/xxxx.py ```

### local chain

```

> brownie run scripts/showLocalRun.py 


Brownie v1.17.2 - Python development framework for Ethereum

BrownieplayProject is the active project.

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

```