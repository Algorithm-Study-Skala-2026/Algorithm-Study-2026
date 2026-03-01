# 나머지 합 구하기 문제

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * n
C = [0] * m
answer = 0

for i in range(n):
    if i == 0:
        S[i] = A[i]
    else:
        S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] >= 2:
        answer += C[i] * (C[i] - 1) // 2

print(answer)

# 구간 합 배열과 나머지 연산의 성질을 결합하여 해결했음.
# (A+B) % M = ((A%M) + (B%M)) % M 성질에 의해, S[i] % M == S[j] % M 이면 (S[i] - S[j]) % M == 0 이 성립.
# 따라서 구간 합 배열의 각 원소를 M으로 나눈 나머지를 카운트 배열 C에 저장하고, 같은 나머지를 가진 인덱스 쌍의 수를 조합 공식 C[i] * (C[i]-1) / 2 로 구해 누적했음.
