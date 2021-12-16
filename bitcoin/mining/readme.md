# mining
* The purpose of mining is not the creation of new bitcoin. That’s the incentive system. Mining is the mechanism by which bitcoin’s security is decentralized.


Miners receive two types of rewards in return for the security provided by mining: new coins created with each new block, also known as a block reward or coinbase reward, and transaction fees from all the transactions included in the block. To earn this reward, miners compete to solve a difficult mathematical problem based on a cryptographic hash algorithm. The solution to the problem, called the Proof-of-Work, is included in the new block and acts as proof that the miner expended significant computing effort. The competition to solve the Proof-of-Work algorithm to earn the reward and the right to record transactions on the blockchain is the basis for bitcoin’s security model.


* [consensus](consensus.md)

## process

* (1) set Coinbase Transaction ([coinbase](coinbaseTransaction.md))
* (2) Constructing the Block Header
   *	add the "Previous Block Hash"
   *	summarize all the transactions with a merkle tree
   *	add a 4-byte timestamp
   *	fills in the target [target](target.md)
   *	initialized to zero the nonce

* The goal is now to find a value for the nonce that results in a block header hash that is equal to or less than the target. 
* The hash function SHA256 is the function used in bitcoin’s mining process
* In the simplest terms, mining is the process of hashing the block header repeatedly, changing one parameter, until the resulting hash matches a specific targe
* see [proff of work](proffOfWrk.md)
 

