from checkout import Checkout
co1 = Checkout()
co1.new('pricing_rules.txt')

co1.scan('A')
co1.scan('B')
co1.scan('A')
co1.scan('A')
co1.scan('B')
co1.scan('C')

print 'The bill is ', co1.total()
