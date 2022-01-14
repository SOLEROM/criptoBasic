# tests

* scema

```

def test_XXXX():
    # Arrange
    # Act
    # Assert

```
* see example at ./browniePlay/tests/test_simple_storage.py

* run 

```
> brownie test  //run all tests
> brownie test -k test_XXXX //will run only certain test
> brownie test  --pdb  //get shell when test fail to play in

```