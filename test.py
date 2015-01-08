from sample_checkout import Checkout
co1 = Checkout()
co1.new('default.txt')
print co1.scan('A')
print co1.scan('B')
print co1.scan('C')
print 'The bill is ', co1.total()
