# about

* [blockStruct](blockStruct.md)
* [genesisBlock](genesisBlock.md)
* [merkleTrees](merkleTrees.md)
* [nonProduction](nonProduction.md)
* [play2](play2.md)


## history immutable

The "previous block hash" field is inside the block header and thereby affects the current block’s hash. The child’s own identity changes if the parent’s identity changes. When the parent is modified in any way, the parent’s hash changes. The parent’s changed hash necessitates a change in the "previous block hash" pointer of the child. This in turn causes the child’s hash to change, which requires a change in the pointer of the grandchild, which in turn changes the grandchild, and so on. This cascade effect ensures that once a block has many generations following it, it cannot be changed without forcing a recalculation of all subsequent blocks. Because such a recalculation would require enormous computation (and therefore energy consumption), the existence of a long chain of blocks makes the blockchain’s deep history immutable, which is a key feature of bitcoin’s security.

## Block Identifiers

* (1) Block Header Hash -  The primary identifier of a block is its cryptographic hash, a digital fingerprint, made by hashing the block header twice through the SHA256 algorithm.
* (2) block height -  position in the blockchain
* Unlike the block hash, the block height is not a unique identifier
* 
