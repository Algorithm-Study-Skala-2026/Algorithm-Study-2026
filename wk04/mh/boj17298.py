import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = [-1]*N

stack = []

for i in range(N):
    cur_val = A[i]
    while stack:
        if stack[-1][1] < cur_val:
            NGE[stack.pop()[0]] = cur_val
        else:
            break
    stack.append((i, A[i]))

while stack:
    NGE[stack.pop()[0]] = -1

sys.stdout.write(' '.join(map(str, NGE)))