from checkout import Checkout
co1 = Checkout()
co1.new('pricing_rules.txt')

print co1.scan('A')
print co1.scan('B')
print co1.scan('A')
print co1.scan('A')

print 'The bill is ', co1.total()
