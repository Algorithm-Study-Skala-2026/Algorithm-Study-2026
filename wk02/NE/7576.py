import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs():
    q = deque()
    for j in range(n):
        for i in range(m):
            if grid[j][i] == 1:
                q.append((j, i))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = grid[ey][ex] + 1
                    q.append((ny, nx))
    max_value = max(max(row) for row in grid) - 1
    for j in range(n):
        for i in range(m):
            if grid[j][i] == 0:
                return -1
    return max_value

print(bfs())