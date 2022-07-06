def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    index = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            answer = max(answer, i+1)
    return answer