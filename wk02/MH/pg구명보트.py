def solution(people, limit):
    table = {}
    people.sort()
    
    left, right = 0, len(people) - 1
    
    count = 0
    while left <= right:
        left_weight = people[left]
        right_weight = people[right]
        if left_weight + right_weight > limit:
            right -=1
        else:
            left += 1
            right -=1
        count+=1
        
    return count