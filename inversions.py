# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if left < right:
        ave = (left + right) // 2
        number_of_inversions += get_number_of_inversions(a, b, left, ave)
        number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
        #write your code here
        number_of_inversions += merge(a,b, left, ave, right)
    return number_of_inversions

def merge(a, b, left, ave, right):
    i = left
    j = ave+1
    k = left
    invCount = 0
    while i <= ave and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            k+=1
            i+=1
        else:
            b[k] = a[j]
            invCount += (ave - i + 1)
            k+=1
            j+=1

    while i<=ave:
        b[k]=a[i]
        k+=1
        i+=1

    while j<=right:
        b[k]=a[j]
        k+=1
        j+=1
    
    for t in range(left , right+1):
        a[t] = b[t]

    return invCount

        
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
