import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    q = deque()
    q.append((y, x))
    chk[y][x] = True
    


for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            minv = min(minv, bfs(j,i))

print(minv)