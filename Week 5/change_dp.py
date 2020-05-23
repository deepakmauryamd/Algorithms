# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,3,4]
    minNumCoins = [0]*(m+1)
    minNumCoins[0] = 0
    for i in range(1, m+1):
        minNumCoins[i] = sys.maxsize
    for i in range(1, m+1):
        for j in range(len(coins)):
            if(i >= coins[j]):
                numCoins = minNumCoins[i-coins[j]] + 1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i] = numCoins
    
    return minNumCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
