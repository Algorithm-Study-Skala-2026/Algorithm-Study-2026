from collections import deque
import heapq
def solution(priorities, location):
    pointer=0
    count=0
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((p, i))
                
    while queue:
        maxp, maxi = max(queue)
        nowp, i = queue.popleft()
        
        if nowp == maxp: 
            count+=1        
            if i==location:
                return count
        elif nowp < maxp:
            queue.append((nowp, i)) 
                        
    return 1