import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_A = [0] * N
sum_A[0] = A[0]


mm = defaultdict(int)

for i in range(1,N):
    sum_A[i] = sum_A[i-1] + A[i]

for i in range(0,N):
    sum_A[i] %= M
    mm[sum_A[i]] +=1

count = 0
for k, v in mm.items():
    if k == 0:
        count+=v
    
    count += int((v*(v-1))/2)

sys.stdout.write(str(count))