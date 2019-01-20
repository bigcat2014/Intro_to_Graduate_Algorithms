#!/usr/bin/python3

# Calculates the nth fibonacci number recursively
# Inputs: n >= 0
# Outputs: The nth fibonacci number
# Running Time O(n^2)


def FIB1(n):
    if n == 0:  # O(1)
        return 0
    elif n == 1:  # O(1)
        return 1
    else:
        # O(n^2)
        return FIB1(n - 1) + FIB1(n - 2)  # O((n-1)^2) + O((n-2)^2)


# Calculates the nth fibonacci number using dynamic programming
# Inputs: n >= 0
# Outputs: The nth fibonacci number
# Running Time O(n)
def FIB2(n):
    F = [0, 1]

    # O(n)
    for i in range(2, n + 1):  # O(n)
        F.append(F[i - 1] + F[i - 2])  # O(1)

    return F[n]
