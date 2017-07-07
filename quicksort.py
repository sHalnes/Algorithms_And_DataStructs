from random import randint

def quicksort(l, lo, hi):
    if lo < hi:
        p1, p2 = partitioning(l, lo, hi)
        quicksort(l, lo, p1)
        quicksort(l, p2, hi)


def partitioning(l, lo, hi):
    pivot = l[randint(lo, hi-1)]
    before = []
    like = []
    after = []
    for i in range(lo, hi):
        if l[i] < pivot:
            before.append(l[i])
        elif l[i] == pivot:
            like.append(l[i])
        else:
            after.append(l[i])
    # fill in array again
    index = lo
    while before:
        l[index] = before.pop()
        index += 1
    p1 = index
    while like:
        l[index] = like.pop()
        index += 1
    p2 = index
    while after:
        l[index] = after.pop()
        index += 1
    return p1, p2



# # helping function to randomize an array before call quicksort function. Without randomization
# # we can get worst case performance (O(N^2)) on an array if an array is already sorted.
# # NB can be used only with small arrays
# def randomize_array(l):
#     for i in range(len(l) - 1):
#         rand_j = randint(i, len(l) - 1)
#         l[i], l[rand_j] = l[rand_j], l[i]
#     return l




unsorted_array = [randint(0, 100) for i in range(20)]
print('Unsorted array: ', unsorted_array)
# unsorted_array = randomize_array(unsorted_array)
# print('Unsorted array after randomizing:\n', unsorted_array)
quicksort(unsorted_array, 0, len(unsorted_array))
print('Sorted array: ', unsorted_array)