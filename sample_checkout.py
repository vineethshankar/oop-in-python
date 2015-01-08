class Checkout:
	def __init__(self):
		self.sum = 0.0
		
	def new(self,filename = 'default.txt'):
		junk = 0
		with open(filename) as f:
			while True:
				line = f.readline()
				junk += 1
				if '---' in line:
					break
				if not line:
					break
			item = []
			cost = []
			for x in f.readlines():
				item.append(x.split()[0])
				cost.append(float(x.split()[1]))
			self.d = dict(zip(item,cost))
				
	def scan(self, s):
		self.sum +=  self.d[s]
		print 'total = '
		return self.sum
		print '\n'
		
	def total(self):
		return self.sum
			
