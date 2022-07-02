def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer

# 프로그래머스 레벨 1 문제 중 고민을 제일 많이 한 문제인듯하다... 이렇게 풀릴줄 상상도 못했다..;;