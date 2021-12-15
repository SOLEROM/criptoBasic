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
