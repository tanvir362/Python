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

class linkedlist:
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
			
if __name__ == "__main__":
	lnkedlist = linkedlist()
	lnkedlist.insert(5)
	lnkedlist.insert(7)
	lnkedlist.insert(1)
	lnkedlist.insert(9)
	lnkedlist.insert(12)
	lnkedlist.insert(14)
	lnkedlist.insert(8)
	lnkedlist.traverse()



