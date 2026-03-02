def solution(n, times):

    left, right = 0, max(times) * n

    while left < right:
        mid = (left + right) // 2
        count = 0
        for t in times:
            count += mid // t
        if count >= n:
            right = mid
        else:
            left = mid + 1
    return left


print(solution(6, [7, 10]))  # testcase: 28