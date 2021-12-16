# target

* defines the required Proof-of-Work to make this a valid block. 
* The target is stored in the block as a "target bits" metric, which is a mantissa-exponent encoding of the target. 
* The encoding has a 1-byte exponent, followed by a 3-byte mantissa (coefficient)

* example (block 277,316)

```
the target bits value is 0x1903a30c. 
 The first part 0x19 is a hexadecimal exponent, 
 the next part, 0x03a30c, is the coefficient.

```

* formula to calculate the difficulty target 

```
target = coefficient * 2^(8*(exponent–3))

```

```

    target = 0x03a30c * 20x08*(0x19-0x03)
    => target = 0x03a30c * 2(0x08*0x16)
    => target = 0x03a30c * 20xB0

which in decimal is:

    => target = 238,348 * 2176
    => target =
    22,829,202,948,393,929,850,749,706,076,701,368,331,072,452,018,388,575,715,328

switching back to hexadecimal:

    => target =
    0x0000000000000003A30C00000000000000000000000000000000000000000000


```


## Adjust Difficulty

* Bitcoin’s blocks are generated every 10 minutes, on average. This is bitcoin’s heartbeat and underpins the frequency of currency issuance and the speed of transaction settlement
* Retargeting occurs automatically and on every node independently. 
* Every 2,016 blocks, all nodes retarget the Proof-of-Work
* The equation for retargeting measures the time it took to find the last 2,016 blocks and compares that to the expected time of 20,160 minutes (2,016 blocks times the desired 10-minute block interval)
* The ratio between the actual timespan and desired timespan is calculated and a proportionate adjustment (up or down) is made to the target
* If the network is finding blocks faster than every 10 minutes, the difficulty increases (target decreases). If block discovery is slower than expected, the difficulty decreases (target increases)

```


New Target = Old Target * (Actual Time of Last 2016 Blocks / 20160 minutes)


```
