# coinbase transaction

* The first transaction in any block is a special transaction, called a coinbase transaction.
* This transaction is constructed by the miner node and contains his reward for the mining effort.
* Unlike regular transactions, the coinbase transaction does not consume (spend) UTXO as inputs. 
* it has only one input, called the coinbase, which creates bitcoin from nothing.

##  exmaple 

* (1) coinbase fee of the block to the miner : 25.09094928

```at the block there are  total transaction fees of 0.09094928 bitcoin
When block 277,316 was mined, the reward was 25 bitcoin per block
```

* (2) target

```


$ bitcoin-cli getblockhash 277316

0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4

$ bitcoin-cli getblock 0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4

{
    "hash" : "0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4",
    "confirmations" : 35561,
    "size" : 218629,
    "height" : 277316,
    "version" : 2,
    "merkleroot" : "c91c008c26e50763e9f548bb8b2fc323735f73577effbc55502c51eb4cc7cf2e",
    "tx" : [
        "d5ada064c6417ca25c4308bd158c34b77e1c0eca2a73cda16c737e7424afba2f",


        ... 417 more transactions ...

       ],
    "time" : 1388185914,
    "nonce" : 924591752,
    "bits" : "1903a30c",				//(2)
    "difficulty" : 1180923195.25802612,
    "chainwork" : "000000000000000000000000000000000000000000000934695e92aaf53afa1a",
    "previousblockhash" : "0000000000000002a7bbd25a417c0374cc55261021e8a9ca74442b01284f0569"
}





$ bitcoin-cli getrawtransaction d5ada064c6417ca25c4308bd158c34b77e1c0eca2a73cda16c737e7424afba2f 1

{
    "hex" : "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0f03443b0403858402062f503253482fffffffff0110c08d9500000000232102aa970c592640d19de03ff6f329d6fd2eecb023263b9ba5d1b81c29b523da8b21ac00000000",
    "txid" : "d5ada064c6417ca25c4308bd158c34b77e1c0eca2a73cda16c737e7424afba2f",
    "version" : 1,
    "locktime" : 0,
    "vin" : [
        {
            "coinbase" : "03443b0403858402062f503253482f",
            "sequence" : 4294967295
        }
    ],
    "vout" : [
        {
            "value" : 25.09094928,				//(1)
            "n" : 0,
            "scriptPubKey" : {
                "asm" : "02aa970c592640d19de03ff6f329d6fd2eecb023263b9ba5d1b81c29b523da8b21OP_CHECKSIG",
                "hex" : "2102aa970c592640d19de03ff6f329d6fd2eecb023263b9ba5d1b81c29b523da8b21ac",
                "reqSigs" : 1,
                "type" : "pubkey",
                "addresses" : [
                    "1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N"
                ]
            }
        }
    ]
}


```


## coinbase data
* must be between 2 and 100 bytes. 
* Except for the first few bytes, the rest of the coinbase data can be used by miners in any way they want; it is arbitrary data.
* As per BIP-34, version-2 blocks (blocks with the version field set to 2) must contain the block height index


* example

````
            "coinbase" : "03443b0403858402062f503253482f",

03, instructs the script execution engine to push the next three bytes onto the script stack
0x443b04, are the block height encoded in little-endian format 
		0x443b04 => 0x043b44 = 277,316

0385840206 are used to encode an extra nonce - used to find a suitable Proof-of-Work solution.

2f503253482f is the ASCII-encoded string /P2SH/, which indicates that the mining node that mined this block provides support for the P2SH improvement defined in BIP-16



```
