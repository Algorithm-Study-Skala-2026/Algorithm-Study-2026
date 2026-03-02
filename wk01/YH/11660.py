# 구간 합 구하기 문제

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0] * (n + 1)]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    A.append(row)

D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
    
# 질의가 최대 100,000개이므로 매 질의마다 합을 구하면 시간 초과가 발생, 이를 해결하기 위해 2차원 구간 합 배열 사용(강의 내용 참고함).
# D[i][j]를 (0,0)부터 (i,j)까지의 합으로 정의하고, D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j] 공식으로 합 배열을 채웠음.
# 이후 D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1] 공식으로 O(1)에 처리.
  