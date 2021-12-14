# Network Discovery

* When a new node boots up, it must discover other Bitcoin nodes on the network in order to participate.
* To connect to a known peer, nodes establish a TCP connection, usually to port 8333
* Upon establishing a connection, the node will start a "handshake" 

```



nVersion

    The bitcoin P2P protocol version the client "speaks" (e.g., 70002)
nLocalServices

    A list of local services supported by the node, currently just NODE_NETWORK
nTime

    The current time
addrYou

    The IP address of the remote node as seen from this node
addrMe

    The IP address of the local node, as discovered by the local node
subver

    A sub-version showing the type of software running on this node (e.g., /Satoshi:0.9.2.1/)
BestHeight

    The block height of this node’s blockchain


```
