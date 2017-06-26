from random import randint
from linked_list_1 import *

def unsorted_list(n):
    unsorted = LinkedList()
    for i in range(n):
        unsorted.add_node(randint(1, 100))
    return unsorted

def selection_sort(unsorted_l):
    sorted_list = LinkedList()
    for i in range(unsorted_l.length):
        min = unsorted_l.find_min()
        unsorted_l.del_node(min)
        sorted_list.add_node(min)
    return sorted_list



n = 20
unsorted_l = unsorted_list(n)
print('Unsorted: ', unsorted_l)
sorted_l = selection_sort(unsorted_l)
print('Sorted: ', sorted_l)