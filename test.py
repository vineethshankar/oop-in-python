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
			print junk
			for x in f.readlines():
				item.append(x.split()[0])
				cost.append(float(x.split()[1]))
				d = dict(zip(item,cost))
