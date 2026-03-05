import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX + 1)

def bfs(start):
    q = deque([start])
    dist[start] = 0
    
    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
        
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
                
print(bfs(n))