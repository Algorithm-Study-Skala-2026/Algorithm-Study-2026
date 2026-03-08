import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
answer = [-1]*n
mystack = []

for i in range(n):
  while mystack and A[mystack[-1]] < A[i]:
    answer[mystack.pop()] = A[i]
  mystack.append(i)

print(*answer)
