# Uses python3
def edit_distance(s, t):
    #write your code here
    result = [[x for x in range(len(s)+1)] for y in range(len(t)+1)]
    
    for y in range(len(t) + 1):
        result[y][0] = y
    
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            ins = result[j-1][i] + 1
            dele = result[j][i-1] + 1
            match = result[j-1][i-1]
            mismatch = result[j-1][i-1] + 1
            if s[i-1] == t[j-1]:
                result[j][i] = min(ins, dele, match)
            else:
                result[j][i] = min(ins, dele, mismatch)

    return result[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
