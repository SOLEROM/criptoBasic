# BIP-65

* BIP-65 (CHECKLOCKTIMEVERIFY) reinterpreted the NOP2 opcode. Clients implementing BIP-65 interpret NOP2 as OP_CHECKLOCKTIMEVERIFY and impose an absolute locktime consensus rule on UTXO that contain this opcode in their locking scripts.


