class Checkout:
	offer_acount = 3
	offer_aprice = 130.0

	def __init__(self):
		self.sum = 0.0
		
	def new(self,filename = 'default.txt'): # Reads the pricing rules
		junk = 0                            # Creates dictionary
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
			item_count = []
			for x in f.readlines():
				item.append(x.split()[0])
				cost.append(float(x.split()[1]))
				item_count.append(0) # Initializing counts to 0
			self.d = dict(zip(item,cost))
			self.dcount = dict(zip(item,item_count))
				
	def scan(self, s):
		self.dcount[s] += 1
		if self.dcount[s]%self.offer_acount == 0: # some function of s here instead of offer_acount
			self.sum += self.offer_aprice - (self.offer_acount-1)*self.d[s]
#			self.sum =  (self.dcount[s]%self.offer_acount)*self.d[s] +(self.dcount[s]/self.offer_acount)*self.offer_aprice
		else:
			self.sum += self.d[s]
		print 'total = '
		return self.sum
		print '\n'
		
	def total(self):
		return self.sum
			
