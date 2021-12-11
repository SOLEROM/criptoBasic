# bx tool

## Elliptic Curve play

```
bx help seed
    Usage: bx seed [-h] [--bit_length value] [--config value]
    Info: Generate a pseudorandom seed.

bx seed
b4cce89be81f7b8b4589790f030c6d6bef1cb3487dface8b
bx seed
3a2658d1b7d2ea2f6aac585d38b8e99451e0cc73cf5d22d7


```

```
bx help ec-new
    Usage: bx ec-new [-h] [--config value] [SEED]
    Info: Create a new Base16 EC private key from entropy.

bx seed | bx ec-new 
137dd31546c899bc4eb3b30cce839e9e0b537db1666b26c163ffab71e32bbd55

```

```
bx help ec-to-wif
  Usage: bx ec-to-wif [-hu] [--config value] [--version value]
  [EC_PRIVATE_KEY]
  Info: Convert an EC private key to a WIF private key. The result
  associates with the compressed public key format by default.


bx seed | bx ec-new | bx ec-to-wif
L3PAbzgVviysRU6qiAQcdpBMGctiGK8Fqvd8uuStEw9Mp7N7swsb



```

### 

```
bx seed | bx ec-new 
      8b5505a092df1580508ed919677a0eae4a5ec35a966c47cd09062172b7b0b88e
echo  8b5505a092df1580508ed919677a0eae4a5ec35a966c47cd09062172b7b0b88e | bx ec-to-wif
      L1tZ6x9u3xFhVFXP7v4BrmwiHjcPtzvsbNTtFzovq9XRzG8Y6wEe

```

```
//private
//Create a new Base16 EC private key from entropy
bx seed | bx ec-new
      8b5505a092df1580508ed919677a0eae4a5ec35a966c47cd09062172b7b0b88e

//private-WIF
//Convert an EC private key to a WIF private key
echo  8b5505a092df1580508ed919677a0eae4a5ec35a966c47cd09062172b7b0b88e | bx ec-to-wif
      L1tZ6x9u3xFhVFXP7v4BrmwiHjcPtzvsbNTtFzovq9XRzG8Y6wEe


//public
//Derive the EC public key of an EC private key.public
bx ec-to-public 8b5505a092df1580508ed919677a0eae4a5ec35a966c47cd09062172b7b0b88e
      026c7afd4b518aee97398f814f78a07f4ceb0bf7b74ec26c3a62415e0e22100ced

//Convert an EC public key to a payment address.
bx ec-to-address 026c7afd4b518aee97398f814f78a07f4ceb0bf7b74ec26c3a62415e0e22100ced
1ENMRpKspV7bSbGhnVZ7Yiy7PCSYKzu62Y


```



