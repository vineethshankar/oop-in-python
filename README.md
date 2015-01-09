## Supermarket checkout system: oop-in-python
This is a python implementation of the 9th recommended exercise in [CodeKata](http://codekata.com/kata/kata09-back-to-the-checkout/ "Kata 09").

Here, a checkout system has been designed in which items can be 'scanned' and prices tallied in accordance to a user-set pricing rules. The default pricing rules are given in [default.txt](https://github.com/vineethshankar/oop-in-python/blob/master/default.txt).

The interface to this checkout system is contained in [test.py](https://github.com/vineethshankar/oop-in-python/blob/master/test.py).

```python
co1 = Checkout()
co1.new('pricing_rules.txt')
co1.scan('A')
co1.scan('B')
co1.scan('A')
co1.scan('A')
co1.scan('B')
co1.scan('C')
print 'The bill is ', co1.total()
```
