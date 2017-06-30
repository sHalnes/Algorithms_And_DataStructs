class Node:
    def __init__(self, header = None, next = None):
        self.top = header
        self.next = next

    def __str__(self):
        return str(self.top)

    def get_top(self):
        return self.top

    def get_next(self):
        return self.next

    def set_next(self, new_link):
        self.next = new_link



class LinkedList:
    def __init__(self):
        self.head = Node('Sentinel')
        self.length = 0

    def add_node(self, header):
        node = Node(header)
        if self.head.get_next() is None:
            self.head.set_next(node)
        else:
            node.set_next(self.head.get_next())
            self.head.set_next(node)
        self.length += 1

    def add_last(self, header):
        node = Node(header)
        current_node = self.head.get_next()
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(node)
        self.length += 1

    def __str__(self):
        l = []
        current_node = self.head.next
        while current_node is not None:
            l.append(str(current_node))
            current_node = current_node.get_next()
        return('-->'.join(l))

    def insert(self, new_header, add_after_node):
        current_node = self.head.get_next()
        new_node = Node(new_header)
        initial_length = self.length
        while current_node is not None:
            if current_node.get_top() == add_after_node:
                new_node.set_next(current_node.get_next())
                current_node.set_next(new_node)
                self.length += 1
                break
            current_node = current_node.get_next()

        # this piece need to be changed
        #if current_node.get_next() is None:
        if initial_length == self.length:
            print('There is no node {} in the list'.format(add_after_node))

    def has_node(self, target):
        current_node = self.head.get_next()
        while current_node.get_next() is not None:
            if current_node.get_top() == target:
                return True
            current_node = current_node.get_next()
        return False


    def get_size(self):
        return self.length

    def is_empty(self):
        return self.head.next == None

    def del_node(self, node_to_del):
        '''delete an element from the linked list'''
        current_node = self.head
        while current_node.get_next() is not None:
            if current_node.get_next().get_top() == node_to_del:
                node_after_delited = current_node.get_next()
                current_node.set_next(node_after_delited.get_next())
                self.length -= 1
                break
            current_node = current_node.get_next()


    def find_min(self):
        '''returns the min element'''
        current_node = self.head.get_next()#.get_top()
        min = current_node.get_top()
        while current_node.get_next() is not None:
            if min > current_node.get_next().get_top():
                min = current_node.get_next().get_top()
            current_node = current_node.get_next()
        return min



# ll = LinkedList()
# print('Create linked list')
# ll.add_node(1)
# print('add node 1')
# ll.add_node(2)
# print('add node 2')
# ll.add_node(7)
# print('add node 7')
# ll.add_node(8)
# print('add node 8\n')
#
# print('\nlist size: ', ll.get_size())
# print(ll)
#
# print('\ninsert node 5 after node 1')
# ll.insert(5, 1)
#
# print('list size: ', ll.get_size())
# print(ll)
#
# print('\ninsert node 5 after node 6')
# ll.insert(5, 6)
#
# print('\ndo we have node 56?')
# print(ll.has_node(56))
# print('\ndo we have node 7?')
# print(ll.has_node(7))
#
# print('\ndelite node 8')
# ll.del_node(8)
# print(ll)
#
# print(ll.head.get_next().get_top())
# print(ll.find_min())
#
# ll.add_last(12)
# print(ll)