# abstract data types - ADT
# stack is ADT.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])



# stack = Stack()
# stack.push('cow')
# stack.push('hamster')
# stack.push('cat')
# stack.push('dog')
# print(stack.is_empty())
# while not stack.is_empty():
#     print(stack.pop())
# print(stack.is_empty())
