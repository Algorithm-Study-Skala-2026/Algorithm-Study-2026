import sys
input = sys.stdin.readline
N = int(input())
T = [0]
P = [0]
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

T += [0]
P += [0]

dp = [0] * (N+2)
for i in range(0, N+2):
    for j in range(0, i): 
        if j+T[j] <= i:
            dp[i] = max(dp[i], dp[j]+P[j])
            # print(i, dp[i], dp[j],'+', P[j])
    
sys.stdout.write(str(dp[N+1]))