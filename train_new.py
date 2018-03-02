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
