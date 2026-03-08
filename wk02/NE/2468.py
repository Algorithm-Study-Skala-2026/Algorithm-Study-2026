import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
building = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(sy, sx, h, visited):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N:
                if building[ny][nx] > h and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

answer = 0

for h in range(0, 101):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for y in range(N):
        for x in range(N):
            if building[y][x] > h and not visited[y][x]:
                bfs(y, x, h, visited)
                count += 1

    answer = max(answer, count)

print(answer)