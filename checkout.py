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
			item = [] # Stores all items
			cost = [] # Store unit prices of each item
			item_count = [] # Counts for each item
			item_special = [] # Stores items with special offers
			item_offer = [] # What is the offer
			
			for x in f.readlines():
				print x.split()
				print '\n'
				item.append(x.split()[0])
				cost.append(float(x.split()[1]))
				item_count.append(0) # Initializing counts for each item
				if len(x.split()) > 2:
					item_special.append(x.split()[0])
					item_offer.append([float(x.split()[2]),float(x.split()[4])])
			self.d = dict(zip(item,cost))
			self.dcount = dict(zip(item,item_count))
			self.doffer = dict(zip(item_special, item_offer))
			print self.doffer['B'][1]
			print self.dcount
	def scan(self, s):
		self.dcount[s] += 1
		if s in self.doffer.keys() and self.dcount[s]%self.doffer[s][0] == 0: # condition for offer qualification
				self.sum += self.doffer[s][1] - (self.doffer[s][0]-1)*self.d[s]
#			self.sum =  (self.dcount[s]%self.offer_acount)*self.d[s] +(self.dcount[s]/self.offer_acount)*self.offer_aprice
		else:
			self.sum += self.d[s]
		print 'total = '
		return self.sum
		print '\n'
		
	def total(self):
		return self.sum
			
