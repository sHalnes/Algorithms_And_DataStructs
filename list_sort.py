# An algorithm to sort list with data where data are ages of clients in range 0-130 (we are optimists!)

from random import randint
import time

# create a list of random ages
unsorted_array = [randint(0, 130) for x in range(100000)]


def sorting():
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

    # # this alternative is faster
    # for i in range(len(ages)):
    #     if ages[i] > 0:
    #         temp = ages[i]*[i]
    #         sorted_array += temp


# this part just to find out the faster alternative
time_list = []
n = 1000

for i in range(n):
    t = time.process_time()
    sorting()
    elapsed_time = time.process_time() - t
    time_list.append(elapsed_time)

avg_time = sum(time_list)/n
print('average time', avg_time)
