def merge(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    result = []
    c1 = 0
    c2 = 0
    while len(result) < len(l1) + len(l2):
        if c1 < len(l1) and c2 < len(l2):
            if l1[c1] < l2[c2]:
                result.append(l1[c1])
                c1 += 1
            else:
                result.append(l2[c2])
                c2 += 1
        elif c1 == len(l1):
            result += l2[c2:]
        else:
            result += l1[c1:]
    return result

def mergesort(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    return merge(mergesort(l[: mid]), mergesort(l[mid : ]))


l = [100, 80, 70, 16, 67, 37, 66, 42, 18, 31, 82, 23, 78, 35, 2, 60, 67, 61, 13, 66, 60, 11, 67, 23, 78, 42, 61, 23, 58, 75, 14, 57, 6, 30, 48, 31, 64, 95, 37, 19]
print(l)
print(mergesort(l))





