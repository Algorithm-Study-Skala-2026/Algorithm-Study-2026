# 최솟값 찾기 문제

import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
now = list(map(int, input().split()))

mydeque = deque()
result = []

for i in range(n):

    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    
    mydeque.append((now[i], i))
    
    while mydeque[0][1] < i - l + 1:
        mydeque.popleft()
    
    result.append(mydeque[0][0])

print(*result)

# N이 최대 5,000,000으로 정렬을 사용하면 O(NlogN)으로 시간 초과가 발생하므로, 덱(deque)을 이용한 # 슬라이딩 윈도우로 O(N)에 해결(강의 내용 참고함).
# 덱에 (값, 인덱스) 쌍을 저장하며, 새 값이 들어올 때 덱의 오른쪽에서 현재 값보다 큰 요소를 제거하고, 왼쪽에서 윈도우 범위(i-L+1)를 벗어난 요소를 제거함.
# 이렇게 하면 덱의 왼쪽 끝이 항상 현재 윈도우의 최솟값을 가리키게 됨.
  