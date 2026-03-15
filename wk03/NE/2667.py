import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    graph[y][x] = 0
    count = 1
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0 <= ny < N and 0 <= nx < N:
            if graph[ny][nx] == 1:
                count += dfs(ny,nx)
                
    return count

result = []

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            result.append(dfs(y,x))

result.sort()

print(len(result))
for r in result:
    print(r)