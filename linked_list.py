class node:
	def __init__(self, data=None, next_node=Node):
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
		start = node()

	def insert(self, data):
		newnd = node(data, start.next_node)
		self.start.set_next(newnd)

	def traverse(self, data):
		current = start
		while current.next_node != None:
			current = current.next_node
			print(current.data)
			

