# Flow Control 

* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch07.asciidoc#scripts-with-flow-control-conditional-clauses


## stack syntex

Pseudocode of flow control in most programming languages

```
if (condition):
  code to run when condition is true
else:
  code to run when condition is false
code to run in either case

```

In a stack-based language like Bitcoin Script, the logical condition comes before the IF, which makes it look "backward," like this:
Bitcoin Script flow control


````
condition
IF
  code to run when condition is true
ELSE
  code to run when condition is false
ENDIF
code to run in either case



````
