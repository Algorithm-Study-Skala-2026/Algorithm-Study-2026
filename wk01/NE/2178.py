import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    q = deque()
    q.append((y, x))
    chk[y][x] = True

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if grid[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny, nx))
                    grid[ny][nx] = grid[ey][ex] + 1
    return grid[n-1][m-1]

print(bfs(0,0))