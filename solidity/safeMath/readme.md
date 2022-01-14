 

 https://openzeppelin.com/

safe math
https://docs.openzeppelin.com/contracts/4.x/utilities#api:math.adoc#SafeMath

```

import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract XXXX {
// safe math library check uint256 for integer overflows
using SafeMathChainlink for uint256;


...

}

```
