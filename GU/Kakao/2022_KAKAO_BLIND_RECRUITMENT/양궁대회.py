from collections import Counter
from itertools import combinations_with_replacement as combis
import sys
from copy import deepcopy

max_score_diff = -sys.maxsize
lion_arrow = [0 for _ in range(11)]
candidates = []
p_arrow = []


def get_score(lion, pitch):
    lion_score, pitch_score = 0, 0
    for idx, (l, p) in enumerate(zip(lion, pitch)):
        if l > p:
            lion_score += (10-idx)
        elif l < p:
            pitch_score += (10-idx)
        elif l == 0 and p == 0:
            continue
        else:  # 둘이 같을 경우
            pitch_score += (10-idx)
    return lion_score, pitch_score


def solution(n, info):
    global candidates, p_arrow
    answer = []
    p_arrow = info
    recursive(n, lion_arrow)

    if len(candidates) == 0:
        answer.append(-1)
    else:
        pass
    return answer


def recursive(n, l_arrow):
    global p_arrow, max_score_diff, candidates
    if n == 0:
        #print('l_arrow:', l_arrow)
        lion_score, pitch_score = get_score(l_arrow, p_arrow)
        lion_arrow = deepcopy(l_arrow)
        score_diff = abs(lion_score-pitch_score)
        if lion_score > pitch_score:
            if max_score_diff < score_diff:
                max_score_diff = score_diff
                candidates = [lion_arrow]
                print(l_arrow, '대입:', lion_arrow)
            elif max_score_diff == score_diff:
                candidates.append(lion_arrow)
                print(l_arrow, max_score_diff, score_diff, '추가:', lion_arrow)
            else:
                pass
        return
    for i in range(11):
        l_arrow[i] += 1
        recursive(n-1, l_arrow)
        l_arrow[i] -= 1


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])


# Other answer


def combination(n, info):
    global answer, max_point
    # 0 ~ 11까지 n개 중복조합 뽑기 ex.(1, 1, 1, 1, 1)
    if n == 5:
        print(list(combis(range(11), n)))

    for combi in combis(range(11), n):
        # Counter를 통해 각 원소의 개수 구하기 ex.Counter({1: 5})
        cnt = Counter(combi)
        apeach, lion = 0, 0
        # 점수계산
        for i in range(11):
            if info[10-i] < cnt[i]:
                lion += i
            elif info[10-i] > 0:
                apeach += i
        if lion-apeach > max_point:
            max_point = lion-apeach
            for i in range(11):
                answer[10-i] = cnt[i]


def solution(n, info):
    global answer, max_point
    answer = [0]*11
    max_point = 0
    combination(n, info)
    if max_point == 0:
        answer = [-1]
    return answer


'''
#Remind
1. from collections import Counter
Counter를 사용하면 dict type으로 갯수를 셀 수 있다.
2. from itertools import combinations_with_replacement as combis
combinations_with_replacement를 사용하면 중복조합 사용 가능: (1,1,1,1,4) etc...
3.   for i in range(11):
            if i >= ex_num:
                lion[i] += 1
                dfs(depth+1, i)
                lion[i] -= 1
이렇게 쓰면 경우의수가 중복 되지 않게 할 수 있다.->위의 코드가 경우의 수를 중복시키게 하지 않는(4,1,0,0,0 이 나왓는데 다음에 
4,1,0,0,0 이 나오는 것을 방지해준다.)중복 순열 코드이다.
'''
