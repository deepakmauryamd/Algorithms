#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = []
    a.sort()
    while(len(a) > 0):
        maxDigit = 0
        for digit in a:
            if(isGreaterOrEqual(digit, maxDigit)):
                maxDigit = digit
        res.append(maxDigit)
        a.remove(maxDigit)
    return ''.join(res)

def isGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
