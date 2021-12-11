# 

## explorer view
![](./explore1_1.png)

* raw view: see [explore1](explore1.md) 


## Transaction chain

![](trans1.png)

## output

* (1) integer denominated in satoshis
* (2) cryptographic puzzle that sets the conditions for spending

```
"vout": [
  {
    "value": 0.01500000,      //(1)
    "scriptPubKey": "OP_DUP OP_HASH160 ab68025513c3dbd2f7b92a94e0581f5d50f654e7 OP_EQUALVERIFY    //(2)
    OP_CHECKSIG"
  },
  {
    "value": 0.08450000,
    "scriptPubKey": "OP_DUP OP_HASH160 7f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a8 OP_EQUALVERIFY OP_CHECKSIG",
  }
]


```
## input

* transaction ID, referencing the transaction that contains the UTXO being spent
* identifying which UTXO from that transaction is referenced
* conditions placed on the UTXO, unlocking it for spending
* A sequence number


```
"vin": [
  {
    "txid": "7957a35fe64f80d234d76d83a2a8f1a0d8149a41d81de548f0a65a8a999f6f18",       //(1)
    "vout": 0,
    "scriptSig" : "3045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e3813[ALL] 0484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adf",
    "sequence": 4294967295
  }
]

```

