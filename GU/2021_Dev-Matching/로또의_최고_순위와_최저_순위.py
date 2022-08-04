def solution(lottos, win_nums):
    answer = []
    correct, unknown = 0, 0
    for number in lottos:
        if number == 0:
            unknown += 1
            continue
            
        if number in win_nums:
            correct += 1
    best = correct + unknown
    worst = correct
    answer.append(7-best  if best>=2 else 6)
    answer.append(7-worst if worst>=2 else 6)
    return answer