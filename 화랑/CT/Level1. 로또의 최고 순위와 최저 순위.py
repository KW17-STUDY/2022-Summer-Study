def solution(lottos, win_nums):
    answer = []
    prize = {'6':1, '5':2, '4':3, '3':4, '2':5, '1':6, '0':6}
    count_0 = lottos.count(0)
    match = 0
    for i in win_nums:
        if i in lottos:
            match += 1
    answer.append(prize[str(match+count_0)])
    answer.append(prize[str(match)])
    return answer