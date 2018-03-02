

import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
car0 = int(sys.stdin.readline())
lower = [-car0]
higher = []
for i in range(n-1):
    car = int(sys.stdin.readline())
    if car > car0:
        higher.append(car)
    else:
        lower.append(-car)
#print(lower)
#print(higher)

def LIS(sequence):
    if len(sequence) == 0:
        return 0
    else:
        LIS_sequence = [1]*len(sequence)
        for i in range(1,len(sequence)):
            for j in range(0,i):
                if sequence[i] > sequence[j]:
                    LIS_sequence[i] = max(LIS_sequence[j] + 1, LIS_sequence[i])

        #print(LIS_sequence)
        return max(LIS_sequence)


total_max = LIS(lower) + LIS(higher)
print(total_max)


# l = []
# l.append((0,1))
# l
# [(0, 1)]
# l.append((1,2))
# l
# [(0, 1), (1, 2)]
# b= (6,7)
# s = l.pop()[:]+b[:]
# s
# (1, 2, 6, 7)
# l.append((0,1))
# l
# [(0, 1), (0, 1)]
# st = set()
# st.add((0,1))
# st.add((2,3))
# v = st.pop()[:-1] + s[:]
# v
# (0, 1, 2, 6, 7)
# st.add(v)
# st
# {(2, 3), (0, 1, 2, 6, 7)}
# len(s)
# 4



'''


import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
all_cars = []
for i in range(n):
    car = int(sys.stdin.readline())
    all_cars.append(car)

def LIS(sequence):
    LIS_sequence = [1]*len(sequence)
    LIS_sequence_low = [1]*len(sequence)
    for i in range(1,len(sequence)):
        for j in range(0,i):
            if sequence[i] > sequence[j]:
                LIS_sequence[i] = max(LIS_sequence[j] + 1, LIS_sequence[i])
            elif -sequence[i] > -sequence[j]:
                LIS_sequence_low[i] = max(LIS_sequence_low[j] + 1,LIS_sequence_low[i])
    print(all_cars)
    print(LIS_sequence)
    print(LIS_sequence_low)
    return max(LIS_sequence)+max(LIS_sequence_low)


total_max = LIS(all_cars)
print(total_max)


6
1
2
4
3
5
6
    elif
        higher.append(car)
        if higher[-1] < higher[-2]:
            higher_up = False
    else:
        is_sorted = False
        lower.append(-car)
        if lower[-1] < lower[-2]:
            lower_down = False
def LIS(sequence, growing):
    print('in lis')
    if sequence and growing:
        return len(sequence)
    elif sequence:
        new_seq = [[sequence[0]]]
        for i in range(1, len(sequence)):
            for j in range(len(new_seq)):
                if new_seq[j][-1] > sequence[i]:
                    new_seq[j][-1] = sequence[i]
                    #break
                elif new_seq[j][-1] < sequence[i]:
                    new_seq.append(new_seq[j] + [sequence[i]])
        max_length = 0
        print('finish with sorting, finding max length')
        for i in range(len(new_seq)):
            if len(new_seq[i]) > max_length:
                max_length = len(new_seq[i])
        return max_length

    else:
        return 1


if is_sorted and higher_up:
    print(n)

else:
    low = LIS(lower, lower_down)
    print('low:', low)
    high = LIS(higher, higher_up)
    print('high:', high)
    total_max = low+high-1
    #total_max = LIS(lower, lower_down) + LIS(higher, higher_up) - 1
    print(total_max)


# longest increasing subsequence

#sequence generator
# import random
# def generator():
#     tall_set = set()
#     with open('trains_4.in', 'w') as file:
#         file.write('1000\n')
#         for i in range(1000):
#             file.write(str(i)+'\n')
#         #while len(tall_set) <1000:
#         #    tall = random.randint(1,10001)
#         #    tall_set.add(tall)
#         #while tall_set:
#         #    file.write(str(tall_set.pop())+'\n')
#     print('finish')
# generator()

'''

'''

import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
car0 = int(sys.stdin.readline())
# lower_down = True
# higher_up = True
lower = []
higher = []
temp_l = [-car0]
temp_h = [car0]
# is_sorted = True
for i in range(n - 1):
    car = int(sys.stdin.readline())
    if car > car0:
        # print(temp_h)
        if car - temp_h[-1] == 1:
            temp_h.append(car)
        else:
            higher.append(temp_h.copy())
            temp_h = [car]

    else:
        # print(temp_l)
        if -car - temp_l[-1] == 1:
            temp_l.append(-car)
        else:
            lower.append(temp_l.copy())
            temp_l = [-car]

higher.append(temp_h)
lower.append(temp_l)
# in case we have well sorted sequence
if len(lower) == 1 and len(higher) == 1:
    print(len(lower[0]) if len(lower[0]) > len(higher[0]) and len(higher[0]) == 1 else len(higher[0]))
    sys.exit()

def LIS(sequence):
    # print('in lis')
    if len(sequence) == 1:
        return len(sequence[0])
    else:
        new_seq = [sequence[0]]
        for i in range(1, len(sequence)):
#            print(i, 'sequence[i]: ', sequence[i])
#            print('our new_seq now:', new_seq)
            print(new_seq)
            # probably the problem is here, since list is dynamically changed, we iterate through new list at the same time
            # possible solution: do not add new lists here, but use a temp list variable.
            for j in range(len(new_seq)):
                #print('\t\tj', j)
                #print('new_seq[-(j+1)][-1], sequence[i][0]', new_seq[-(j+1)][-1], sequence[i][0])
                if new_seq[j][-1] > sequence[i][0] and new_seq[j][-2] < sequence[i][0]:
                    #print('new_seq[-(j+1)][-1] > sequence[i][0] and new_seq[-(j+1)][-2] < sequence[i][0]', new_seq[-(j+1)][-1], '>', sequence[i][0])
                    #print(new_seq[-(j+1)][-2], '<', sequence[i][0])
                    new_seq[j] = new_seq[j][:-1] + sequence[i]
                    #print('new swq after adding ',new_seq[-(j+1)])
                    #break
                # here! if we start from zero it will be always less!
                if new_seq[j][-1] < sequence[i][0]:
                    #print('new_seq[-(j+1)][-1] < sequence[i][0]',new_seq[-(j+1)][-1], ' < ', sequence[i][0])
                    new_seq.append(new_seq[j] + sequence[i])
                    #print('we added: ', new_seq[-1])
                    #break
        max_length = 0
        for i in range(len(new_seq)):
            if len(new_seq[i]) > max_length:
                max_length = len(new_seq[i])
                #print(new_seq[i])
        #print(new_seq)
        #return len(new_seq[-1])
        return max_length


total_max = LIS(lower) + LIS(higher) - 1
print(total_max)




import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
car0 = int(sys.stdin.readline())
#lower_down = True
#higher_up = True
lower = []
higher = []
temp_l = [-car0]
temp_h = [car0]
#is_sorted = True
for i in range(n - 1):
    car = int(sys.stdin.readline())
    if car > car0:
        #print(temp_h)
        if temp_l:
            lower.append(temp_l.copy())
            temp_l = []
        if temp_h and car - temp_h[-1]==1:
            temp_h.append(car)
        elif temp_h:
            higher.append(temp_h.copy())
            temp_h = [car]
        else:
            temp_h.append(car)
    else:
        #print(temp_l)
        if temp_h:
            higher.append(temp_h.copy())
            temp_h = []
        if temp_l and -car - temp_l[-1]==1:
            temp_l.append(-car)
        elif temp_l:
            lower.append(temp_l.copy())
            temp_l = [-car]
        else:
            temp_l.append(-car)
if temp_h:
    higher.append(temp_h)
if temp_l:
    lower.append(temp_l)
# in case we have well sorted sequence
if len(lower) == 1 and len(higher) == 1:
    print(len(lower[0]) if len(lower[0])>len(higher[0]) and len(higher[0]) == 1 else len(higher[0]))
    sys.exit()
#print(higher)
#print(lower)

def LIS(sequence):
    #print('in lis')
    if len(sequence) == 1:
        return len(sequence[0])
    else:
        new_seq = [sequence[0]]
        for i in range(1, len(sequence)):
            for j in range(len(new_seq)):
                #print('new_seq[j][-1][-1], sequence[i][0]', new_seq[j][-1], sequence[i][0])
                if new_seq[j][-1] > sequence[i][0]:
                    new_seq[j] = new_seq[j][:-2]+sequence[i]
                    #print('new swq after adding ',new_seq)
                    #break
                elif new_seq[j][-1] < sequence[i][0]:
                    new_seq.append(new_seq[j] + sequence[i])
                    #print('another one', new_seq)
        max_length = 0
        #print('finish with sorting, finding max length')
        #print(new_seq)
        for i in range(len(new_seq)):
            if len(new_seq[i]) > max_length:
                max_length = len(new_seq[i])
        return max_length


total_max = LIS(lower) + LIS(higher) - 1
print(total_max)






import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
car0 = int(sys.stdin.readline())
lower_down = True
higher_up = True
lower = [-car0]
higher = [car0]
is_sorted = True
for i in range(n - 1):
    car = int(sys.stdin.readline())
    if car > car0:
        higher.append(car)
        if higher[-1] < higher[-2]:
            higher_up = False
    else:
        is_sorted = False
        lower.append(-car)
        if lower[-1] < lower[-2]:
            lower_down = False
def LIS(sequence, growing):
    print('in lis')
    if sequence and growing:
        return len(sequence)
    elif sequence:
        new_seq = [[sequence[0]]]
        for i in range(1, len(sequence)):
            for j in range(len(new_seq)):
                if new_seq[j][-1] > sequence[i]:
                    new_seq[j][-1] = sequence[i]
                    #break
                elif new_seq[j][-1] < sequence[i]:
                    new_seq.append(new_seq[j] + [sequence[i]])
        max_length = 0
        print('finish with sorting, finding max length')
        for i in range(len(new_seq)):
            if len(new_seq[i]) > max_length:
                max_length = len(new_seq[i])
        return max_length

    else:
        return 1


if is_sorted and higher_up:
    print(n)

else:
    low = LIS(lower, lower_down)
    print('low:', low)
    high = LIS(higher, higher_up)
    print('high:', high)
    total_max = low+high-1
    #total_max = LIS(lower, lower_down) + LIS(higher, higher_up) - 1
    print(total_max)






import sys
n = int(sys.stdin.readline())
car0 = int(sys.stdin.readline())

lower = [-car0]
higher = [car0]
for i in range(n-1):
    car = int(sys.stdin.readline())
    if car > car0:
        higher.append(car)
    else:
        lower.append(-car)

def LIS(sequence):
    if sequence:
        new_seq = [[sequence[0]]]
        for i in range(1, len(sequence)):
            for j in range(len(new_seq)):
                if new_seq[j][-1] > sequence[i]:
                    new_seq[j][-1] = sequence[i]
                    break
                elif new_seq[j][-1] < sequence[i]:
                    new_seq.append(new_seq[j] + [sequence[i]])
        return len(new_seq[-1])
    return 1

total_max = LIS(lower) + LIS(higher) -1
print(total_max)




import sys
n = int(sys.stdin.readline())
counter = 0
car0 = int(sys.stdin.readline())
minimum = [[-car0]]
maximum = [[car0]]
for i in range(n-1):
    car = int(sys.stdin.readline())
    if car > car0:
        for j in range(len(maximum)):
            if maximum[j][-1] > car:
                maximum[j][-1] = car
            elif maximum[j][-1] < car:
                maximum.append(maximum[j] + [car])
    else:
        for j in range(len(minimum)):
            if minimum[j][-1] > -car:
                minimum[j][-1] = -car
            elif minimum[j][-1] < -car:
                minimum.append(minimum[j] + [-car])
# now we take lists with maximum length from both minimum and maximum
max_min = len(minimum[-1])
max_max = len(maximum[-1])

total_max = max_min + max_max -1
print(total_max)





import sys
n = int(sys.stdin.readline())
counter = 0
car0 = int(sys.stdin.readline())
minimum = [[-car0]]
maximum = [[car0]]
for i in range(n-1):
    car = int(sys.stdin.readline())
    if car > car0:
        for j in range(len(maximum)):
            if maximum[j][-1] > car:
                maximum[j][-1] = car
            elif maximum[j][-1] < car:
                maximum.append(maximum[j] + [car])
    else:
        for j in range(len(minimum)):
            if minimum[j][-1] > -car:
                minimum[j][-1] = -car
            elif minimum[j][-1] < -car:
                minimum.append(minimum[j] + [-car])
# now we take lists with maximum length from both minimum and maximum
max_min = 0
for i in range(len(minimum)):
    if max_min < len(minimum[i]):
        max_min = len(minimum[i])

max_max = 0
for i in range(len(maximum)):
    if max_max < len(maximum[i]):
        max_max = len(maximum[i])

total_max = max_min + max_max -1
print(total_max)





import sys
n = int(sys.stdin.readline())
counter = 0
car0 = int(sys.stdin.readline())
minimum = []
maximum = [car0]
for i in range(n-1):
    car = int(sys.stdin.readline())
    if car > maximum[0]:
        maximum.append(car)
    else:
        minimum.append(-car)
#here we need to optimize to something less ike O(n^2), O(n log n) would be nice to get
def find_LIS(seq):
    l = [[seq[0]]]
    for i in range(1, len(seq)):
        for j in range(len(l)):
            if l[j][-1] > seq[i]:
                l[j][-1] = seq[i]
            elif l[j][-1] < seq[i]:# and len(l[j]) + 1 > len(new_l):
                l.append(l[j]+[seq[i]])
    max = 0
    for i in range(len(l)):
        if max < len(l[i]):
            max = len(l[i])
    return (max)

if len(maximum) > 0:
    counter += find_LIS(maximum)
if len(minimum) > 0:
    counter += find_LIS(minimum)
print(counter)




# last version with run time error

import sys
n = int(sys.stdin.readline())
counter = 0
car0 = int(sys.stdin.readline())
minimum = []
maximum = [car0]
for i in range(n-1):
    car = int(sys.stdin.readline())
    if car > maximum[0]:
        maximum.append(car)
    else:
        minimum.append(-car)
#here we need to optimize to something less ike O(n^2), O(n log n) would be nice to get
def find_LIS(seq):
    l = [[seq[0]]]
    for i in range(1, len(seq)):
        new_l = []
        for j in range(len(l)):
            if l[-(j+1)][-1] < seq[i] and len(l[-(j+1)]) + 1 > len(new_l):
                new_l = l[-(j+1)]+[seq[i]]
        if len(new_l) > 0:
            l.append(new_l)
        else:
            l.append([seq[i]])
    max = 0
    for i in range(len(l)):
        if max < len(l[i]):
            max = len(l[i])
    return (max)

if len(maximum) > 0:
    counter += find_LIS(maximum)
if len(minimum) > 0:
    counter += find_LIS(minimum)
print(counter)





import sys
n = int(sys.stdin.readline())
minimum = 0
maximum = 0
counter = 0
for i in range(n):
    train = int(sys.stdin.readline())
    if i == 0:
        minimum = maximum = train
        counter += 1
    else:
        if train < minimum:
            minimum = train
            counter += 1
        elif train > maximum:
            maximum = train
            counter += 1
print(counter)


seq = [3, 10, 2, 1, 20]#[3, 2]#[50, 3, 10, 7, 40, 80]#[3,2,6,4,5,1]
l = [[seq[0]]]
for i in range(1, len(seq)):
    new_l = []
    for j in range(len(l)):
        if l[-(j+1)][-1] < seq[i] and len(l[-(j+1)]) + 1 > len(new_l):
            new_l = l[-(j+1)]+[seq[i]]
    if len(new_l) > 0:
        l.append(new_l)
    l.append([seq[i]])
max = 0
for i in range(len(l)):
    if max < len(l[i]):
        max = len(l[i])
print(max)

Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}'''


