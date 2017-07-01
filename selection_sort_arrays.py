from random import randint

# O(N^2)
def selection_sort(l):
    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            min_element = i
            if l[j] < l[min_element]:
                min_element = j
            l[i], l[min_element] = l[min_element], l[i]
    return l


l = [randint(0, 100) for x in range(20)]
print(l)
sorted_arr = selection_sort(l)
print(sorted_arr)