class Heap:

    def __init__(self):
        self.heap = []
        self.length = 0

    def __str__(self):
        return str(self.heap)

    def add_node(self, node):
        self.heap.append(node)
        self.length += 1
        if self.length > 1:
            self.make_heap_up()

    def make_heap_up(self):
        index = self.length - 1
        while True:
            parent = int((index - 1) / 2)
            if self.heap[parent] < self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def make_heap_down(self):
        index = 0
        while True:
            child_1 = 2*index + 1
            child_2 = 2*index + 2
            if child_2 < self.length and child_1 < self.length:
                child = child_1 if self.heap[child_1] > self.heap[child_2] else child_2
                if self.heap[index] < self.heap[child]:
                    self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                    index = child
                else:
                    break
            elif (child_2 >= self.length and child_1 < self.length) or (child_2 < self.length and child_1 >= self.length):
                child = min(child_2, child_1)
                if self.heap[index] < self.heap[child]:
                    self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                    index = child
                else:
                    break
            else:
                break

    def get_root(self):
        root = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        del self.heap[self.length - 1]
        self.length -= 1
        self.make_heap_down()
        return root


tree_elements = [7, 1, 10, 4, 6, 9, 2, 11, 3, 5, 12, 8]
heap = Heap()
for i in tree_elements:
    heap.add_node(i)
print('Heap: ', heap)

while True:
    print('Taking the root:', heap.get_root())
    print('Heap now: ', heap)

    if heap.length < 1:
        break