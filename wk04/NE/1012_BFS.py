import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        cy, cx = queue.popleft()

        for dy, dx in directions:
            ny = cy + dy
            nx = cx + dx

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())  # m: 가로, n: 세로
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    count = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(y, x)
                count += 1

    print(count)