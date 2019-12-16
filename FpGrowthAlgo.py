class FpNode:
	def __init__(self):
		self.parent = None
		self.child = []
		self.item = {}


import operator
class FpGrowthTree:
	def __init__(self, transactions, L1):
		self.Null = FpNode()
		self.transactions = []
		self.L1 = dict( sorted(L1.items(), key=operator.itemgetter(1), reverse=True)) #sorting desc order L1 dictionary based on values
		#print(self.L1)
		self.links = {}

		for x in self.L1:
			self.links[x] = []
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
			for itm in row:
				#print(itm)
				#checking if itm presents in current nodes's childs
				found = False
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
					nchild.parent = current
					current = nchild #move to child
					self.links[itm].append(current) #create links

				#print(current.item)

	def traverse_tree(self, node):
		print(node.item)
		for chld in node.child:
			self.traverse_tree(chld)

	def path(self, itm):
		i = 0
		for ocrns in self.links[itm]:
			i = i + 1
			print("Path of occurrence: {}".format(i))
			current = ocrns
			while current.parent.parent != None:
				print(current.parent.item)
				current = current.parent

			print()




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

#print(transactions)
fp_growth_tree = FpGrowthTree(transactions, L1)
#print(fp_growth_tree.transactions)
fp_growth_tree.generate_tree()
print("\nDFS travarsal of Fp Growth Tree:")
fp_growth_tree.traverse_tree(fp_growth_tree.Null)
fp_growth_tree.path('I3')


