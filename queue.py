from linked_list_1 import Node

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None # last element

    def is_empty(self):
        return self.length == 0

    # This method was slow
    # def insert(self, cargo):
    #     node = Node(cargo)
    #     if self.head is None:
    #         self.head = node
    #     else:
    #         current_node = self.head
    #         while current_node.get_next():
    #             current_node = current_node.get_next()
    #         current_node.set_next(node)
    #     self.length += 1

    def insert(self, cargo):
        '''we're keeping track on the last element of the queue so the adding a new element in the queue 
        will take only O(1) constant time instead of O(n) linear time, where n is the size of the queue'''
        node = Node(cargo)
        if self.head is None:
            self.last = self.head = node
        else:
            last_node = self.last
            last_node.set_next(node)
            self.last = last_node.get_next()
        self.length += 1



    def remove(self):
        cargo = self.head.top
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

q = Queue()
q.insert('one')
q.insert('two')
q.insert('hund')
print('is empty? ', q.is_empty())
print(q.remove())
print(q.remove())
print(q.remove())
print('is empty? ', q.is_empty())
