# Uses python3
import sys

def optimal_weight(W, v):
    # write your code here
    value = [[0 for i in range(len(v)+1)] for j in range(W+1)]
    
    for i in range(1, len(v)+1):
        for w in range(1, W+1):
            value[w][i] = value[w][i-1]
            if v[i-1] <= w:
                val = value[w - v[i-1]][i-1] + v[i-1]
                if val > value[w][i]:
                    value[w][i] = val

    return value[-1][-1] 

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
