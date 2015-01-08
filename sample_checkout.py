class Checkout:
	def __init__(self):
		self.sum = 0.0
		
	def rates(self,filename = 'default.txt'):
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
		ch = ch.isupper()
		price = d[ch]
		self.sum += price
		
	def total(self):
		print self.sum
			
