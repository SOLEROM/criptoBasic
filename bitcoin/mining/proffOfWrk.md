# Proof-of-Work

* With SHA256, the output is always 256 bits long


The miner constructs a candidate block filled with transactions. Next, the miner calculates the hash of this block’s header and sees if it is equal to or smaller than the current target. If the hash is greater than the target, the miner will modify the nonce (usually just incrementing it by one) and try again. At the current difficulty in the Bitcoin network, miners have to try quadrillions of times before finding a nonce that results in a low enough block header hash.



