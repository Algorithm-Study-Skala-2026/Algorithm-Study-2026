import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
AA = list(map(int, input().split()))

A = sorted(A)


for target in AA:

    left = 0
    right = len(A) - 1
    res = 0
    while left <= right:
        mid = (left + right)//2
        src = A[mid]
        if src < target:
            left = mid+1
        elif src > target:
            right = mid-1
        elif src == target:
            res = 1 
            break
    print(res)
 