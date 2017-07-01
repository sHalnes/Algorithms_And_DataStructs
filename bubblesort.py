from random import randint

# O(N^2)
def bubblesort(l):
    continue_sorting = True
    while continue_sorting:
        continue_sorting = False
        for i in range(len(l) - 1):
            if l[i+1] < l[i]:
                l[i+1], l[i] = l[i], l[i+1]
                continue_sorting = True
    return l


l = [randint(0, 100) for x in range(20)]
print('Unsorted: ', l)
sorted_arr = bubblesort(l)
print('Sorted: ', sorted_arr)