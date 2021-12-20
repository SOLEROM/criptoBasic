# Payment Channels

Payment channels are a trustless mechanism for exchanging bitcoin transactions between two parties, outside of the Bitcoin blockchain. These transactions, which would be valid if settled on the Bitcoin blockchain, are held off-chain instead, acting as promissory notes for eventual batch settlement. Because the transactions are not settled, they can be exchanged without the usual settlement latency, allowing extremely high transaction throughput, low (submillisecond) latency, and fine (satoshi-level) granularity.


Payment channels are part of the broader concept of a state channel, which represents an off-chain alteration of state, secured by eventual settlement in a blockchain. A payment channel is a state channel where the state being altered is the balance of a virtual currency.


State channels use timelocks to enforce smart contracts across a time dimension.



## Basic Concepts

* A state channel is established between two parties, through a transaction that locks a shared state on the blockchain. 
* This is called the funding transaction or anchor transaction
* This single transaction must be transmitted to the network and mined to establish the channel
* The two parties then exchange signed transactions, called commitment transactions, that alter the initial state
* These transactions are valid transactions in that they could be submitted for settlement by either party0
* In the entire lifetime of the channel, only two transactions need to be submitted for mining on the blockchain: the funding and settlement transactions. In between these two states, the two parties can exchange any number of commitment transactions that are never seen by anyone else, nor submitted to the blockchain.

## using timelocks

* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch12.asciidoc#simple-payment-channel-example

## revocation

* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch12.asciidoc#asymmetric-revocable-commitments


