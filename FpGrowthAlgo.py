class node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_data(self, data):
		self.data = data

	def set_next(self, nxt):
		self.next_node = nxt


class Linkedlist:
	def __init__(self):
		self.start = node()

	def insert(self, data):
		newnd = node(data, self.start.next_node)
		self.start.set_next(newnd)

	def traverse(self):
		current = self.start
		while current.next_node != None:
			current = current.next_node
			print(current.data, end=" ")

		print("\n")


class FpNode:
	def __init__(self):
		self.child = []
		self.item = {}


import operator
class FpGrowthTree:
	def __init__(self, transactions, L1):
		self.Null = FpNode()
		self.transactions = []
		self.L1 = dict( sorted(L1.items(), key=operator.itemgetter(1), reverse=True))
		print(self.L1)
		self.links = {}
		for x in self.L1:
			self.links[x] = Linkedlist()
		indx = 0
		for i in transactions:
			tran = []
			for x in self.L1:
				if x in transactions[indx]:
					tran.append(x)
			self.transactions.append(tran)
			indx = indx + 1
	
	def generate_tree(self):
		#transactions is rearranged based on L1
		for row in self.transactions:
			current = self.Null #start from the root node
			found = False
			for itm in row:
				#print(itm)
				#checking if itm presents in current nodes's childs
				for chld in current.child:
					if itm in chld.item:
						found = True
						chld.item[itm] = chld.item[itm] + 1
						current = chld #move to child
						break
				#create a new child and set sup_cunt 1 if not found
				if found != True:
					nchild = FpNode()
					nchild.item[itm] = 1
					current.child.append(nchild)
					current = nchild #move to child
					self.links[itm].insert(current) #create links


transactions = []
transactions.append(['I1', 'I2', 'I5'])
transactions.append(['I2', 'I4'])
transactions.append(['I2','I3'])
transactions.append(['I1', 'I2', 'I4'])
transactions.append(['I1', 'I3'])
transactions.append(['I2', 'I3'])
transactions.append(['I1', 'I3'])
transactions.append(['I1', 'I2', 'I3', 'I5'])
transactions.append(['I1', 'I2', 'I3'])

L1 = {}
L1['I1'] = 6
L1['I2'] = 7
L1['I3'] = 6
L1['I4'] = 2
L1['I5'] = 2

print(transactions)
fp_growth_tree = FpGrowthTree(transactions, L1)
print(fp_growth_tree.transactions)
fp_growth_tree.generate_tree()


