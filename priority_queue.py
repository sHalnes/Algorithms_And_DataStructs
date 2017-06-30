from linked_list_1 import Node

class PriorityQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def remove(self):
        max_priority = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[max_priority]:
                max_priority = i
        item = self.items[max_priority]
        del self.items[max_priority]
        return item

p_q = PriorityQueue()
l = [23,13, 4, 7, 89]
for element in l:
    p_q.insert(element)
while not p_q.is_empty():
    print(p_q.remove())
