import sys
input = sys.stdin.readline


N, M = map(int, input().split())

board = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(N):
    board[i] = list(map(int, list(input().split())))

for i in range(N):
    for j in range(N):
        if i>0 and j>0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + board[i][j] - dp[i-1][j-1]
        elif j ==0 and i >0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        elif i ==0 and j >0:
            dp[i][j] = dp[i][j-1] + board[i][j]
        else:
            dp[i][j] = board[i][j]


for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    res = dp[x2][y2]
    if x1 > 0:
        res -= dp[x1-1][y2]
    if y1 > 0:
        res -= dp[x2][y1-1]
    if x1 > 0 and y1 > 0:
        res += dp[x1-1][y1-1]
    print(res)