# 오큰수 구하기 문제

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ans = [0] * n
myStack = []

for i in range(n):

    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

print(*ans)


# N이 최대 1,000,000으로 이중 반복문을 사용하면 시간 초과가 발생하므로, 스택(stack)을 활용하여 O(N)에 해결(강의 영상 참고함).
# 스택에는 값이 아닌 인덱스를 저장하며, 새 원소가 스택 top의 수열값보다 크면 top을 pop하고 해당 인덱스의 정답을 현재 값으로 채움.
# 이후 스택에 남은 인덱스는 오큰수가 존재하지 않으므로 -1을 저장.
  