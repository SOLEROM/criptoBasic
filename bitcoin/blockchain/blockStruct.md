# Structure of a Block


```
4 bytes			Block Size		The size of the block, in bytes, following this field
80 bytes		Block Header		Several fields form the block header
1–9 bytes (VarInt)	Transaction Counter 	How many transactions follow
Variable		Transactions		The transactions recorded in this block
```

## Block Header

* three sets of block metadata:

```
(1) a reference to a previous block hash, which connects this block to the previous block in the blockchain
(2) difficulty, timestamp, and nonce, relate to the mining competition
(3) merkle tree root, a data structure used to efficiently summarize all the transactions in the block
```

* The structure of the block header 

```
|  4 bytes | Version | A version number to track software/protocol upgrades
| 32 bytes | Previous Block Hash | A reference to the hash of the previous (parent) block in the chain
| 32 bytes | Merkle Root | A hash of the root of the merkle tree of this block's transactions
|  4 bytes | Timestamp | The approximate creation time of this block (in seconds elapsed since Unix Epoch)
|  4 bytes | Difficulty Target | The Proof-of-Work algorithm difficulty target for this block
|  4 bytes | Nonce | A counter used for the Proof-of-Work algorithm

```


## example

```


$ bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f


{
    "hash" : "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
    "confirmations" : 308321,
    "size" : 285,
    "height" : 0,
    "version" : 1,
    "merkleroot" : "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
    "tx" : [
        "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"
    ],
    "time" : 1231006505,
    "nonce" : 2083236893,
    "bits" : "1d00ffff",
    "difficulty" : 1.00000000,
    "nextblockhash" : "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"
}

```


