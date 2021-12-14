Multisignature

* Multisignature scripts set a condition where N public keys are recorded in the script and at least M of those must provide signatures to unlock the funds. This is also known as an M-of-N scheme, where N is the total number of keys and M is the threshold of signatures required for validation.

* At this time, standard multisignature scripts are limited to at most 3 listed public keys, meaning you can do anything from a 1-of-1 to a 3-of-3 multisignature or any combination within that range
	* check the IsStandard() function to see what is currently accepted by the network

*  P2SH multisignature scripts are limited to 15 keys, allowing for up to 15-of-15 multisignature.

## A bug in CHECKMULTISIG execution
* CHECKMULTISIG will pop an extra value or one value more than expected.
* Because this bug became part of the consensus rules, it must now be replicated forever
* you should expect to see an extra 0 in the beginning, whose only purpose is as a workaround to a bug that accidentally became a consensus rule.

##  
