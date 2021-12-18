# Soft Fork Signaling with Block Version

* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch10.asciidoc#soft-fork-signaling-with-block-version

Since soft forks allow non-upgraded clients to continue to operate within consensus, the mechanism for "activating" a soft fork is through miners signaling readiness: a majority of miners must agree that they are ready and willing to enforce the new consensus rules. To coordinate their actions, there is a signaling mechanism that allows them to show their support for a consensus rule change. This mechanism was introduced with the activation of BIP-34 in March 2013 and replaced by the activation of BIP-9 in July 2016

* https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki
