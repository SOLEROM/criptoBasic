# Validating

* When a node receives a new block, it will validate the block by checking it against a long list of criteria that must all be met; 
* otherwise, the block is rejected. 
* These criteria can be seen in the Bitcoin Core client in the functions CheckBlock and CheckBlockHeader and include:

```

(1)    The block data structure is syntactically valid

(2)    The block header hash is equal to or less than the target (enforces the Proof-of-Work)

(3)    The block timestamp is less than two hours in the future (allowing for time errors)

(4)    The block size is within acceptable limits

(5)    The first transaction (and only the first) is a coinbase transaction

(6)    All transactions within the block are valid using the transaction checklist 

```
