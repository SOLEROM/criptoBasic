#  bloom filters


Because SPV nodes need to retrieve specific transactions in order to selectively verify them, they also create a privacy risk. Unlike full blockchain nodes, which collect all transactions within each block, the SPV node’s requests for specific data can inadvertently reveal the addresses in their wallet. For example, a third party monitoring a network could keep track of all the transactions requested by a wallet on an SPV node and use those to associate Bitcoin addresses with the user of that wallet, destroying the user’s privacy.

Shortly after the introduction of SPV/lightweight nodes, bitcoin developers added a feature called bloom filters to address the privacy risks of SPV nodes. Bloom filters allow SPV nodes to receive a subset of the transactions without revealing precisely which addresses they are interested in, through a filtering mechanism that uses probabilities rather than fixed patterns.


* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch08.asciidoc#bloom-filters
