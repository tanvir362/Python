class LinkedList:
    def __init__(self, data=None, node=None):
        self.data=data
        self.next=node

    def add(self, data):
        if not self.next:
            self.next = LinkedList(data)
        else:
            self.next.add(data)

    def traverse(self):
        if self.data:
            print(self.data, end=" ")
        # else:
        #     print('No data', end=' ')
        if self.next:
            self.next.traverse()

    def find(self, key, indx=-1):
        if self.data == key:
            # print(f'data matched and indx is {indx} data is {self.data}')
            return indx
        if self.next:
            # print(f'data did not match sending {indx+1} to next node data is {self.data}')
            return self.next.find(key, indx+1)
        # print('data did not match at all')
        return -1
    
    def reverse(self):
        if self.next:
            self.next.reverse()
            """
            pointing some node having no value may result to some node point start that  creats a loop
            between start->node->start
            """
            if self.data:
                self.next.next = self
                """
                as the node self is point now pointing self so self don't need to point the node so it's become None now 
                else it may create a loop self->next_node->self
                """
                self.next = None
        else:
            my_list.next = self

my_list = LinkedList(11)
for i in range(1,11):
    my_list.add(i)

my_list.traverse()
print()
# print(my_list.find(50))
my_list.reverse()
my_list.traverse()
print()