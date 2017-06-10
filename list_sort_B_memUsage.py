from random import randint
from memory_profiler import profile

# alternative B

@profile
def sorting():
    # create a list of random ages
    unsorted_array = [randint(0, 130) for x in range(100000)]

    # create an array to hold ages
    ages = [0 for x in range(0, 131)]

    # count how many people have a certain age
    for i in range(len(unsorted_array)):
        ages[unsorted_array[i]] += 1

    # making a sorted array
    sorted_array = []

    # this alternative is faster
    for i in range(len(ages)):
        if ages[i] > 0:
            temp = ages[i]*[i]
            sorted_array += temp

    return sorted_array

if __name__ == '__main__':
    sorting()

'''
Line #    Mem usage    Increment   Line Contents
================================================
     6     21.5 MiB      0.0 MiB   @profile
     7                             def sorting():
     8                                 # create a list of random ages
     9     25.4 MiB      4.0 MiB       unsorted_array = [randint(0, 130) for x in range(100000)]
    10                             
    11                                 # create an array to hold ages
    12     25.1 MiB     -0.3 MiB       ages = [0 for x in range(0, 131)]
    13                             
    14                                 # count how many people have a certain age
    15     25.8 MiB      0.6 MiB       for i in range(len(unsorted_array)):
    16     25.8 MiB      0.0 MiB           ages[unsorted_array[i]] += 1
    17                             
    18                                 # making a sorted array
    19     25.8 MiB      0.0 MiB       sorted_array = []
    20                             
    21                                 # this alternative is faster
    22     26.0 MiB      0.3 MiB       for i in range(len(ages)):
    23     26.0 MiB      0.0 MiB           if ages[i] > 0:
    24     26.0 MiB      0.0 MiB               temp = ages[i]*[i]
    25     26.0 MiB      0.0 MiB               sorted_array += temp
    26                             
    27     25.3 MiB     -0.7 MiB       return sorted_array

'''