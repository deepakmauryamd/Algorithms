# Uses python3
import sys
def min_operations(n):
    result = [0]*(n+1)
    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 3 == 0:
            min3 = result[i//3]
        if i % 2 == 0:
            min2 = result[i//2]
        minOps = min(min1,min2,min3)
        result[i] = minOps+1
    return result

def min_list(n, ops):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0:
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return reversed(sequence)


def optimal_sequence(n):
    if n == 1:
        return [1]
    else:
        ops = min_operations(n)
    return min_list(n, ops)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
