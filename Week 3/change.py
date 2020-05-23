# Uses python3
import sys

def get_change(m):
    #write your code here
    # 1 5 10
    if(m == 1 or m == 5 or m == 10):
        return 1
    else:
        count = 0
        while(m > 0):
            if(m >= 10):
                count += 1
                m = m - 10
            elif(m >= 5):
                count += 1
                m = m - 5
            else:
                count += m
                m = 0
        return count

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
