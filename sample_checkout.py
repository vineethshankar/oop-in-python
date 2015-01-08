class Checkout:
	def __init__(self, input = 'default.txt'):
		self.sum = 0.0
		rates(input)
		
	def rates(filename):
		junk = 0
		with open(filename) as f:
			while True:
				line = f.readline()
				junk += 1
				if '---' in line:
					break
				if not line:
					break
					
			d = {}
			item = []
			cost = []
			for x in f.readlines():
				item.append(x.split()[0])
				cost.append(float(x.split()[1]))
				d = dict(zip(item,cost))
				
	def scan(self, ch):
		ch = is.upper(ch)
		price = d[ch]
		self.sum += price
		
	def total(self):
		print self.sum
			
