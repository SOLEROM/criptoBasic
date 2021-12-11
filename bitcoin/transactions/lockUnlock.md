# locking script and an unlocking

## locking

* A locking script is a spending condition placed on an output 
* the conditions that must be met to spend the output in the future
* called a scriptPubKey, because it usually contained a public key or Bitcoin address (public key hash)
* 

## unlocking
* a script that "solves," or satisfies, the conditions placed on an output by a locking script and allows the output to be spent 
* Most of the time they contain a digital signature produced by the user’s wallet from his or her private key


## validate
* bitcoin validating node will validate transactions by executing the locking and unlocking scripts together
* The validation software will copy the unlocking script, retrieve the UTXO referenced by the input, and copy the locking script from that UTXO
* The unlocking and locking script are then executed in sequence
* The input is valid if the unlocking script satisfies the locking script conditions

![](lock1.png)

## stack example

![](script1.png)

## P2PKH

* majority of transactions processed on the Bitcoin network spend outputs locked with a Pay-to-Public-Key-Hash or "P2PKH" scrip
* These outputs contain a locking script that locks the output to a public key hash, more commonly known as a Bitcoin address
* output locked by a P2PKH script can be unlocked (spent) by presenting a public key and a digital signature created by the corresponding private key


