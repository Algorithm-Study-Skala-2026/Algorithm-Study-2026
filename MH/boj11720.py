import sys
input = sys.stdin.readline

N = int(input())
num_string = input().strip()

res = 0
for num in num_string:
    res += int(num)

sys.stdout.write(str(res))