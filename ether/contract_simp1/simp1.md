# Simple Contract (1)

* https://github.com/ethereumbook/ethereumbook/blob/develop/02intro.asciidoc#a-simple-contract-a-test-ether-faucet

```
/code/Solidity$ cat Faucet.sol 
==============================

// SPDX-License-Identifier: CC-BY-SA-4.0

// Version of Solidity compiler this program was written for
pragma solidity 0.6.4;

// Our first contract is a faucet!
contract Faucet {
    // Accept any incoming amount
    receive() external payable {}

    // Give out ether to anyone who asks
    function withdraw(uint withdraw_amount) public {
        // Limit withdrawal amount
        require(withdraw_amount <= 100000000000000000);

        // Send the amount to the address that requested it
        msg.sender.transfer(withdraw_amount);
    }
}


```



```
/code/Solidity$ cat Faucet.sol
==============================

// SPDX-License-Identifier: CC-BY-SA-4.0

// Version of Solidity compiler this program was written for
pragma solidity 0.6.4;

// Our first contract is a faucet!
contract Faucet { 				### This line declares a contract object, similar to a class declaration
    // Accept any incoming amount
    receive() external payable {}		### enable the contract to accept any incoming amount:
### The receive function is called if the transaction that triggered the contract didn’t name any of the declared functions in the contract,
### or didn’t contain data and thus was a plain Ether transfer
### Contracts can have one such receive function (without a name) and it is used to receive ether
### it is defined as an external and payable function, which means it can accept ether into the contract.
### It doesn’t do anything, other than accept the ether, as indicated by the empty definition in the curly braces ({}
### If we make a transaction that sends ether to the contract address, as if it were a wallet, this function will handle it


    // Give out ether to anyone who asks

### the first function of the Faucet contract
### It is declared as a public function, meaning it can be called by other contracts.
### takes one unsigned integer (uint) argument

    function withdraw(uint withdraw_amount) public {


        // Limit withdrawal amount 
### uses the built-in Solidity function require to test a precondition
### controls the flow of funds out of the contract by placing a limit on withdrawals
        require(withdraw_amount <= 100000000000000000); //= 0.1 ether
###  If the withdraw function is called with a withdraw_amount greater than that amount, the require function here will cause contract execution to stop and fail with an exception

### the actual withdrawal:
### The msg object is one of the inputs that all contracts can access
### msg represents the transaction that triggered the execution of this contract
### attribute sender is the sender address of the transaction
### function transfer is a built-in function that transfers ether from the current contract to the address of the sender.

        // Send the amount to the address that requested it
        msg.sender.transfer(withdraw_amount);
    }
}


```




##


## security
*  flawed contract, demonstrating a number of bad practices and security vulnerabilities.

* 
