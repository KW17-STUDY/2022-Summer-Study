from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    index = deque(i for i in range(len(q)))
    while q:
        temp = q.popleft()
        paper = index.popleft()
        if len(q)!=0 and temp < max(q):
            q.append(temp)
            index.append(paper)
        else:
            answer += 1
            if location==paper:
                break
    return answer