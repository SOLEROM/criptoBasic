# interface

* https://www.npmjs.com/package/@chainlink/contracts
* https://github.com/smartcontractkit/chainlink

## what is interface
* no code just define
* interface compile down to ABI
* ABI tells how to interact with another contract 

```
https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol
=========================================================


interface AggregatorV3Interface {

 function decimals() external view returns (uint8);

  function description() external view returns (string memory);

  function version() external view returns (uint256);

```

* to call for interface function we will need the deployed address
* https://docs.chain.link/docs/ethereum-addresses/

```
ETH / USD 	8 	0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419

```
* https://etherscan.io/address/0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419

