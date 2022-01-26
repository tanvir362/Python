class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
	
	def add(self, data):
		if not self.head:
			self.head = Node(data)
			return
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = Node(data)

	def remove(self, data):
		if not self.head:
			return
		cur = self.head
		prev = self.head
		while cur:
			if cur.data == data:
				if prev:
					prev.next = cur.next
				else :
					prev = cur.next
				# cur.next = None
				return
			prev = cur
			cur = cur.next
	
	def traverse(self):
		if not self.head:
			return
		cur = self.head
		while cur:
			print(cur.data, end=" ")
			cur = cur.next
		print()
		

linkedlist = LinkedList()
for i in range(1, 11):
	linkedlist.add(i)

linkedlist.traverse()
linkedlist.remove(1)
linkedlist.traverse()


