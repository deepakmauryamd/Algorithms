# Uses python3
import sys 

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def isOperator(op):
    if op == '+' or op == '-' or op == '*':
        return True
    return False

def get_maximum_value(dataset):
    #write your code here
    num = []
    opr = []
    tmp = ""
    for i in range(len(dataset)):
        if(isOperator(dataset[i])):
            opr.append(dataset[i])
            num.append(int(tmp))
            tmp=""
        else:
            tmp += dataset[i]
    num.append(int(tmp))
   
    total_length = len(num)
    minVal = [[0 for i in range(total_length)] for i in range(total_length)]
    maxVal = [[0 for i in range(total_length)] for i in range(total_length)]

    for i in range(total_length):
        for j in range(total_length):
            if i == j:
                minVal[i][j] = maxVal[i][j] = num[i]

    for L in range(1, total_length + 1):
        for i in range(total_length - L):
            j = i + L
            minVal[i][j], maxVal[i][j] = MinAndMax(i, j, minVal, maxVal, opr)
    
    return maxVal[0][total_length-1]

def MinAndMax(i, j, minVal, maxVal, opr):
    minValue = sys.maxsize
    maxValue = - (sys.maxsize - 1)
    
    for k in range(i, j):
        a = evalt(minVal[i][k], minVal[k+1][j], opr[k]) 
        b = evalt(maxVal[i][k], minVal[k+1][j], opr[k])
        c = evalt(minVal[i][k], maxVal[k+1][j], opr[k])
        d = evalt(maxVal[i][k], maxVal[k+1][j], opr[k])    

        maxValue, minValue = max(maxValue, a, b, c, d), min(minValue, a, b, c, d)
    
    return minValue,maxValue
        

if __name__ == "__main__":
    print(get_maximum_value(input()))
