import sys
input = sys.stdin.readline

result = 0

def merge_sort(start, end):
  global result
  if end - start < 1:
    return
  mid = (start + end) // 2
  merge_sort(start, mid)
  merge_sort(mid+1, end)
  for i in range(start, end+1):
    tmp[i] = A[i]
  
  k= start
  index1 = start
  index2 = mid+1
  while index1 <= mid and index2 <= end:
    if tmp[index1] <= tmp[index2]:
      A[k] = tmp[index1]
      index1 += 1
    else:
      A[k] = tmp[index2]
      result += index2 - k
      index2 += 1
    k+=1
  while index1 <= mid:
    A[k] = tmp[index1]
    index1 += 1
    k+=1
  while index2 <= end:
    A[k] = tmp[index2]
    index2 += 1
    k+=1

N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
tmp = [0] * int(N+1)

merge_sort(1,N)
print(result)
