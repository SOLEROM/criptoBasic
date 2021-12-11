# Pay-to-Script Hash (P2SH) 

* Bitcoin addresses that begin with the number “3” are pay-to-script hash (P2SH) addresses
* called multisignature or multisig addresses
* it provides the opportunity to add functionality to the address itself
* The requirements are designated at the time the address is created, within the script, and all inputs to this address will be encumbered with the same requirements
* Encoding a P2SH address involves using the same double-hash function as used during creation of a Bitcoin address, only applied on the script instead of the public key:

```
script hash = RIPEMD160(SHA256(script))
```

##  multi-signature address script

* multi-signature feature is designed to require M signatures (also known as the “threshold”) from a total of N keys, known as an M-of-N multisig, where M is equal to or less than N



