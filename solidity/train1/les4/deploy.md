# deploy

* full example at [web3_py_simple_storage/deploy.py ](./web3_py_simple_storage/deploy.py)

* deps install

```bash
    git clone https://github.com/PatrickAlphaC/web3_py_simple_storage.git
    pip install py-solc-x    
```

## get the src

```python
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
```

## compile to parts

```python
from solcx import compile_standard, install_solc


compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)
```

## save

```python
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
```

