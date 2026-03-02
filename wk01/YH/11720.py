# 숫자 합 구하기 문제
  
n = int(input())
numbers = list(input())

sum = 0
for i in numbers:
    sum += int(i)

print(sum)

# 입력받은 숫자 문자열을 list()로 한 자리씩 나누어 저장한 뒤, 각 문자를 int()로 변환하며 누적 합산하는 방식으로 해결.
# 별도의 알고리즘 없이 단순 순회(iteration)만으로 풀 수 있는 문제 였다고 생각함.
