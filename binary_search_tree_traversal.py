import sys
pre_order_traversal_list = []
post_order_traversal_list = []
in_order_traversal_list = []
bfs_traversal_list = []
class Node:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None
    
    def insert(self, n):
        if n < self.value:
            if self.left:
                self.left.insert(n)
            else:
                new_node = Node(n)
                self.left = new_node
        else:
            if self.right:
                self.right.insert(n)
            else:
                new_node = Node(n)
                self.right = new_node

    def pre_order(self):
        # print(self.value, end=' ')
        pre_order_traversal_list.append(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        # print(self.value, end=' ')
        post_order_traversal_list.append(self.value)

    def in_order(self):
        if self.left:
            self.left.in_order()
        # print(self.value, end=' ')
        in_order_traversal_list.append(self.value)
        if self.right:
            self.right.in_order()


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, n):
        if self.root:
            self.root.insert(n)
        else:
            new_node = Node(n)
            self.root = new_node

    def pre_order_traversal(self):
        self.root.pre_order()
        # print()

    def post_order_traversal(self):
        self.root.post_order()
        # print()

    def in_order_traversal(self):
        self.root.in_order()
        # print()

    def bfs_traversal(self):
        q = []
        q.append(self.root)
        while(len(q)):
            cur = q.pop(0)
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
            # print(cur.value, end=' ')
            bfs_traversal_list.append(cur.value)
        # print()

tree = BinarySearchTree()
n = input()
for i in input().split():
    tree.insert(int(i))

tree.pre_order_traversal()
tree.in_order_traversal()
tree.post_order_traversal()
tree.bfs_traversal()
print(*pre_order_traversal_list)
print(*in_order_traversal_list)
print(*post_order_traversal_list)
print(*bfs_traversal_list)