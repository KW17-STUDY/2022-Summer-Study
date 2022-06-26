def solution(absolutes, signs):
    answer = 0
    for index, sign in enumerate(signs):
        if sign:
            answer += absolutes[index]
        else:
            answer -= absolutes[index]
    return answer