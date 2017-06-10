from random import randint
from memory_profiler import profile
import psutil
# alternative A

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

    # here are two alternatives to fill inn the sorted array.

    # this alternative is slower
    for i in range(len(ages)):
        if ages[i] > 0:
            for j in range(ages[i]):
                sorted_array.append(i)

    return sorted_array

if __name__ == '__main__':
    sorting()

'''
Line #    Mem usage    Increment   Line Contents
================================================
     6     11.9 MiB      0.0 MiB   @profile
     7                             def sorting():
     8                                 # create a list of random ages
     9     11.9 MiB      0.0 MiB       unsorted_array = [randint(0, 130) for x in range(100000)]
    10                             
    11                                 # create an array to hold ages
    12      8.5 MiB     -3.4 MiB       ages = [0 for x in range(0, 131)]
    13                             
    14                                 # count how many people have a certain age
    15      8.6 MiB      0.1 MiB       for i in range(len(unsorted_array)):
    16      8.6 MiB      0.0 MiB           ages[unsorted_array[i]] += 1
    17                             
    18                                 # making a sorted array
    19      7.2 MiB     -1.4 MiB       sorted_array = []
    20                             
    21                                 # here are two alternatives to fill inn the sorted array.
    22                             
    23                                 # this alternative is slower
    24      7.6 MiB      0.4 MiB       for i in range(len(ages)):
    25      7.6 MiB      0.0 MiB           if ages[i] > 0:
    26      7.6 MiB      0.0 MiB               for j in range(ages[i]):
    27      7.6 MiB      0.0 MiB                   sorted_array.append(i)
    28                             
    29      7.1 MiB     -0.5 MiB       return sorted_array

Line #    Mem usage    Increment   Line Contents
================================================
     5     20.0 MiB      0.0 MiB   @profile
     6                             def sorting():
     7                                 # create a list of random ages
     8     23.3 MiB      3.3 MiB       unsorted_array = [randint(0, 130) for x in range(100000)]
     9                             
    10                                 # create an array to hold ages
    11     10.0 MiB    -13.3 MiB       ages = [0 for x in range(0, 131)]
    12                             
    13                                 # count how many people have a certain age
    14     10.1 MiB      0.1 MiB       for i in range(len(unsorted_array)):
    15     10.1 MiB      0.0 MiB           ages[unsorted_array[i]] += 1
    16                             
    17                                 # making a sorted array
    18      7.6 MiB     -2.5 MiB       sorted_array = []
    19                             
    20                                 # here are two alternatives to fill inn the sorted array.
    21                             
    22                                 # this alternative is slower
    23      8.6 MiB      1.0 MiB       for i in range(len(ages)):
    24      8.5 MiB     -0.0 MiB           if ages[i] > 0:
    25      8.6 MiB      0.0 MiB               for j in range(ages[i]):
    26      8.6 MiB      0.0 MiB                   sorted_array.append(i)
    27                             
    28      8.6 MiB      0.0 MiB       return sorted_array


Line #    Mem usage    Increment   Line Contents
================================================
     5     21.5 MiB      0.0 MiB   @profile
     6                             def sorting():
     7                                 # create a list of random ages
     8     25.5 MiB      4.0 MiB       unsorted_array = [randint(0, 130) for x in range(100000)]
     9                             
    10                                 # create an array to hold ages
    11     25.5 MiB      0.0 MiB       ages = [0 for x in range(0, 131)]
    12                             
    13                                 # count how many people have a certain age
    14     25.7 MiB      0.2 MiB       for i in range(len(unsorted_array)):
    15     25.7 MiB      0.0 MiB           ages[unsorted_array[i]] += 1
    16                             
    17                                 # making a sorted array
    18     21.7 MiB     -4.0 MiB       sorted_array = []
    19                             
    20                                 # here are two alternatives to fill inn the sorted array.
    21                             
    22                                 # this alternative is slower
    23     22.3 MiB      0.7 MiB       for i in range(len(ages)):
    24     22.3 MiB     -0.0 MiB           if ages[i] > 0:
    25     22.3 MiB      0.0 MiB               for j in range(ages[i]):
    26     22.3 MiB      0.0 MiB                   sorted_array.append(i)
    27                             
    28     22.3 MiB      0.0 MiB       return sorted_array

'''