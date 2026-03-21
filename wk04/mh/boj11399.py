N = int(input())
P = list(map(int, input().split()))
sorted_P = sorted(P, reverse=False)

res = 0
for i in range(N):
    res += sorted_P[i] * (N-i)
print(res)