import sys
input = sys.stdin.read
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N+1)

# 에지 데이터 저장
for i in range(M):
	start, end, time = map(int, input().split())
	edges.append((start,end,time))

distance[1] = 0

for _ in range(N-1):
	for start, end, time in edges:
		if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
			distance[end] = distance[start] + time

myCycle = False

for start, end, time in edges:
	if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
		myCycle = True

if not myCycle:
	for i in range(2, N+1):
		if distance[i] != sys.maxsize:
			print(distance[1])
		else:
			print(-1)
else:
	print(-1)