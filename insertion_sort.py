# hjelpefunksjon.
# Create a linked list of n elements with random numbers to sort.
from random import randint
from linked_list_1 import *

def unsorted_list(n):
    unsorted = LinkedList()
    for i in range(n):
        unsorted.add_node(randint(1, 100))
    return unsorted


def insertionsort(unsorted_l):
    sorted_list = LinkedList()
    # we'll first add the smallest element
    first_element = unsorted_l.find_min()
    sorted_list.add_node(first_element)
    # and delete this element from unsorted list
    unsorted_l.del_node(first_element)

    unsorted_node = unsorted_l.head.get_next()
    while unsorted_node is not None:
        current_node = sorted_list.head.get_next()
        n = unsorted_node.get_top()
        while True:
            if n >= current_node.get_top() and current_node.get_next() is None:
                sorted_list.add_last(n)
                break
            if n >= current_node.get_top() and n < current_node.get_next().get_top():
                sorted_list.insert(n, current_node.get_top())
                break
            current_node = current_node.get_next()
        unsorted_node = unsorted_node.get_next()
    return sorted_list




n = 20
unsorted_l = unsorted_list(n)
print('Unsorted list: ', unsorted_l)
sorted_l = insertionsort(unsorted_l)
print('Sorted list: ', sorted_l)
#print('length of the list', sorted_l.length)