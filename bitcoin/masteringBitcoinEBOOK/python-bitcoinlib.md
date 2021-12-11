# python-bitcoinlib

```
sudo apt-get install python3-bitcoinlib
```

## examples

* get blocks:
```
python3 rpc_example.py

```

* get outputs of tx:

```
python3 rpc_transaction.py
==========================

([u'1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA'], Decimal('0.01500000'))
([u'1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK'], Decimal('0.08450000'))


```

* sum all tx in block

```
python rpc_block.py

('Total value in block: ', Decimal('10322.07722534'))

```

