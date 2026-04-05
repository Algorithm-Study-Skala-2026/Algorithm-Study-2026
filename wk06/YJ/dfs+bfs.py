import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, N+1):
  graph[i].sort()

dfs_result = []
bfs_result = []

def dfs(v):
  visited[v]=True
  dfs_result.append(v)

  for next in graph[v]:
    if not visited[next]:
      dfs(next)

def bfs(v):
  visited[v] = True
  queue = deque([v])

  while queue:
    now = queue.popleft()
    bfs_result.append(now)

    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)

visited = [False] * (N+1)
dfs(V)
visited = [False] * (N+1)
bfs(V)

print(*dfs_result)
print(*bfs_result)
