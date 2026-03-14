# [유클리드 호제법 실전문제] 42 최소 공배수 구하기

t = int(input())

def gcd(a, b):
   if b == 0:
      return a
   else:
      return gcd(b, a%b)

for i in range(t):
   a, b = map(int, input().split())
   result = a * b / gcd(a, b)
   print(int(result))