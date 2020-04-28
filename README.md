# FiniteGroupCalc
Calculates and visualizes the calculation of additive and mutiplicative finite groups. Used for learning and practicing Diffie-Hellman-Key-Exchange.
___
### Preparation:
 * Install the latest version of Python 3
 * Also install the pip package called 'tabulate':
'''python
 python -m pip install tabulate
'''
### How to use
#### python getOrder.py [ma] [groupSize] [number]
 * Use m or a parameter for multiplicative or additive group.
 * groupSize is NOT the cardinality or the order, it is Z<sub>n</sub> where n is the 'size'.

### Examples:
```
$ python .\getOrder.py m 5              
#########
2 * 2 = 4 mod 5
4 * 2 = 3 mod 5
3 * 2 = 1 mod 5
#########
3 * 3 = 4 mod 5
4 * 3 = 2 mod 5
2 * 3 = 1 mod 5
#########
4 * 4 = 1 mod 5
#########
  a    ord(a)
---  --------
  1         1
  2         4
  3         4
  4         2
___
$ python .\getOrder.py a 2142124 12874
ord(12874) is: 1071062
___
$ python .\getOrder.py m 521423 21234
##### (huge calculation, to be improved)
ord(21234) is: 223464
```
