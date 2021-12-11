# bitcoind

```
bitcoind -printtoconsole

Config file: /home/XXXX/.bitcoin/bitcoin.conf 

```

## full

```
alertnotify=myemailscript.sh "Alert: %s"
datadir=/lotsofspace/bitcoin
txindex=1

```


## resource-constrained 

```
alertnotify=myemailscript.sh "Alert: %s"
maxconnections=15
prune=5000
dbcache=150
maxmempool=150
maxreceivebuffer=2500
maxsendbuffer=500

```
