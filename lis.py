# Calculates the length of the longest increasing subsequence of a given list
# Inputs: list of numbers
# Outputs: length of the longest increasing subsequence
# Running time: O(n^2)


def LIS(a):
    L = []

    # O(n^2)
    for i in range(len(a)):  # O(n)
        L.append(1)
        for j in range(i + 1):  # O(n)
            if a[j] < a[i] and L[i] < (1 + L[j]):  # O(1)
                L[i] = 1 + L[j]

    max_index = 0

    # O(n)
    for i in range(len(a)):  # O(n)
        if L[i] > L[max_index]:  # O(1)
            max_index = i

    return L[max_index]
