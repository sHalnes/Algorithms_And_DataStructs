from stack import *

def reversing_array(array):
    a_stack = Stack()
    for element in array:
        a_stack.push(element)
    new_array = []
    while a_stack.is_empty() is False:
        new_array.append(a_stack.pop())
    return new_array



array = [x for x in range(10)]
print(array)
reversed_array = reversing_array(array)
print(reversed_array)