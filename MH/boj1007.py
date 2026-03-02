import sys

input = sys.stdin.readline

def dfs(points, N, candidates):
    visited = [0] * N
    for i in range(N):
        print(i)
        if i ==0:
            candidates = []
        if not visited[i]:
            visited[i] = 1
            candidates.append(i)
            dfs(points, N, candidates)
            visited[i] = 0
    print(candidates)
    return

T = int(input())
for t in range(T):
    N = int(input())
    points = set()
    for i in range(N):
        x, y = map(int, input().split()) 
        points.add((x,y))
    
    print(points)
    dfs(points, len(points), [])

