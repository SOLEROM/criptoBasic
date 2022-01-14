# magic


```
public

view

paybale

```


## mapping

```

    //mapping to store which address depositeded how much ETH
    mapping(address => uint256) public addressToAmountFunded;
```

## msg
 keywords of the one called the contract
```
addressToAmountFunded[msg.sender] += msg.value;
```


## keyworks
```
using A for B
//used to attach library functions in a contex to contract
//attach function A to type B
```

## raise

```
 10 ** 18

```

## require

* require if false will revert

```
require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");
```

## this 

* "this" - the contract you are in

```
address(this)  // adress of this contract
```

## balance
* 

## modifier
* modifier is used to change the behaviour of the function

```
modifier onlyOwner {
        _;   //if start here run the code before
        require(msg.sender == owner);
        _;   //mean run the rest of the code from here
    }

// then the call function will be:
    function withdraw() payable onlyOwner public {


```
 
