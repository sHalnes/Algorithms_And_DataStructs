from random import randint

# O(N^2)
def insertion_sort(l):
    for i in range(len(l)-1):
        for j in range(i, len(l)):
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]
    return l


l = [randint(0,100) for x in range(20)]
print(insertion_sort(l))