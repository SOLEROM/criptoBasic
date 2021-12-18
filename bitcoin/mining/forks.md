# forks

* summing the work recorded in each block in a chain, a node can calculate the total amount of work that has been expended to create that chain
* As long as all nodes select the greatest-cumulative-work chain, the global Bitcoin network eventually converges to a consistent state.
* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch10.asciidoc#blockchain-forks

* Bitcoin’s block interval of 10 minutes is a design compromise between fast confirmation times (settlement of transactions) and the probability of a fork. A faster block time would make transactions clear faster but lead to more frequent blockchain forks, whereas a slower block time would decrease the number of forks but make settlement slower.
