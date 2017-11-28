from random import randint

def subsequence(sequence):
    ''' Find largest increasing subsequence.
    Example: sequence [5, 2, 8, 6, 3, 6, 9, 7]
    Answer: [2, 3, 6, 9] or [2, 3, 6, 7] both correct
    '''

    # Make list for possible subsequences
    L = [[x] for x in sequence]

    # Make dictionary for every element in sequence, where elements are keys and values are indeces of smaller previous elements
    D = {}
    for i in range(len(sequence)):
        D[i] = []
        for j in range(i):
            if j != i and sequence[j] < sequence[i]:
                D[i].append(j)

    # Make subsequences
    for i in range(len(sequence)):
        if len(D[i]) > 0:
            edges = D[i]
            max_L = -1
            temp_max_L = [] #temp_max_l = L[x].copy() to copy a list
            # finding the max subsequence
            for j in edges:
                if len(L[j]) > max_L:
                    max_L = len(L[j])
                    temp_max_L = L[j].copy()
            L[i] = temp_max_L + [sequence[i]]

    # Find largest increasing sequence
    largest_seq = []
    for seq in L:
        if len(seq) > len(largest_seq):
            largest_seq = seq.copy()
    print(largest_seq)



# Test solution
sequence = [randint(0, 100) for x in range(20)]
print(sequence)
#s = [5,2,8,6,3,6,9,7]
subsequence(sequence)