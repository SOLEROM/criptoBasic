# test explore


* get block info

```
node@bitcoin:~$ bitcoin-cli getblockstats 1000
{
  "avgfee": 0,
  "avgfeerate": 0,
  "avgtxsize": 0,
  "blockhash": "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09",
  "feerate_percentiles": [
    0,
    0,
    0,
    0,
    0
  ],
  "height": 1000,
  "ins": 0,
  "maxfee": 0,
  "maxfeerate": 0,
  "maxtxsize": 0,
  "medianfee": 0,
  "mediantime": 1232344831,
  "mediantxsize": 0,
  "minfee": 0,
  "minfeerate": 0,
  "mintxsize": 0,
  "outs": 1,
  "subsidy": 5000000000,
  "swtotal_size": 0,
  "swtotal_weight": 0,
  "swtxs": 0,
  "time": 1232346882,
  "total_out": 0,
  "total_size": 0,
  "total_weight": 0,
  "totalfee": 0,
  "txs": 1,
  "utxo_increase": 1,
  "utxo_size_inc": 117
}
```

* get block data

```
node@bitcoin:~$ bitcoin-cli getblockhash 1000
00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09

node@bitcoin:~$ bitcoin-cli getblock 00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09
{
  "hash": "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09",
  "confirmations": 100282,
  "height": 1000,
  "version": 1,
  "versionHex": "00000001",
  "merkleroot": "fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33",
  "time": 1232346882,
  "mediantime": 1232344831,
  "nonce": 2595206198,
  "bits": "1d00ffff",
  "difficulty": 1,
  "chainwork": "000000000000000000000000000000000000000000000000000003e903e903e9",
  "nTx": 1,
  "previousblockhash": "0000000008e647742775a230787d66fdf92c46a48c896bfbc85cdc8acc67e87d",
  "nextblockhash": "00000000a2887344f8db859e372e7e4bc26b23b9de340f725afbf2edb265b4c6",
  "strippedsize": 216,
  "size": 216,
  "weight": 864,
  "tx": [
    "fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33"
  ]
}
```

* get tx

```
node@bitcoin:~$ bitcoin-cli getrawtransaction fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33
01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0804ffff001d02fd04ffffffff0100f2052a01000000434104f5eeb2b10c944c6b9fbcfff94c35bdeecd93df977882babc7f3a2cf7f5c81d3b09a68db7f0e04f21de5d4230e75e6dbe7ad16eefe0d4325a62067dc6f369446aac00000000
node@bitcoin:~$ bitcoin-cli decoderawtransaction `bitcoin-cli getrawtransaction fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33`
{
  "txid": "fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33",
  "hash": "fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33",
  "version": 1,
  "size": 135,
  "vsize": 135,
  "weight": 540,
  "locktime": 0,
  "vin": [
    {
      "coinbase": "04ffff001d02fd04",
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 50.00000000,
      "n": 0,
      "scriptPubKey": {
        "asm": "04f5eeb2b10c944c6b9fbcfff94c35bdeecd93df977882babc7f3a2cf7f5c81d3b09a68db7f0e04f21de5d4230e75e6dbe7ad16eefe0d4325a62067dc6f369446a OP_CHECKSIG",
        "hex": "4104f5eeb2b10c944c6b9fbcfff94c35bdeecd93df977882babc7f3a2cf7f5c81d3b09a68db7f0e04f21de5d4230e75e6dbe7ad16eefe0d4325a62067dc6f369446aac",
        "type": "pubkey"
      }
    }
  ]
}
```


