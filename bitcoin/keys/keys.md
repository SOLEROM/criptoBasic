# keys


![](./keysIdea1.png)

## bitcoin client


*

```
$ bitcoin-cli getnewaddress
1J7mdg5rbQyUHENYdx39WVWK7fsLpEoXZy


=======================================================================
getnewaddress ( "label" "address_type" )

Returns a new Bitcoin address for receiving payments.
If 'label' is specified, it is added to the address book 
so payments received with the address will be associated with 'label'.

Arguments:
1. label           (string, optional, default="") The label name for the address to be linked to. It can also be set to the empty string "" to represent the default label. The label does not need to exist, it will be created if there is no label by the given name.
2. address_type    (string, optional, default=set by -addresstype) The address type to use. Options are "legacy", "p2sh-segwit", and "bech32".

Result:
"str"    (string) The new bitcoin address
=======================================================================

```

```
//expose the private key
//shows the private key in a Base58 checksum-encoded format called the Wallet Import Format (WIF)
$ bitcoin-cli dumpprivkey 1J7mdg5rbQyUHENYdx39WVWK7fsLpEoXZy
KxFC1jmwwCoACiCAWZ3eXa96mBM6tb3TYzGmf6YwgdGWZgawvrtJ



========================================================================
dumpprivkey "address"

Reveals the private key corresponding to 'address'.
Then the importprivkey can be used with this output

Arguments:
1. address    (string, required) The bitcoin address for the private key

Result:
"str"    (string) The private key


=======================================================================



## bitcoint explorer
```


**** [bx tools](../bitcoinExplorer/bxTool.md)
