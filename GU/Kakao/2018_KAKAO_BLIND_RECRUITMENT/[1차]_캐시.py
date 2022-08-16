#13분
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue =  deque([])
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            answer += 5
            queue.append(city)
            if len(queue) > cacheSize:
                queue.popleft()
    return answer