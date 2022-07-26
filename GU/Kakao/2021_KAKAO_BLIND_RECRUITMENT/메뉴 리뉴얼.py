from collections import Counter
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    candidates = defaultdict(int)
    comb = defaultdict(list)
    count = [0 for _ in range(max(course)+1)]

    for order in orders:
        order = sorted(list(order))
        for num in course:
            combination = combinations(order, num)
            for i in combination:
                name_str = ''.join(i)
                candidates[name_str] += 1
                if candidates[name_str] < 2:
                    continue
                if count[num] < candidates[name_str]:
                    comb[num] = [i]
                    count[num] = candidates[name_str]
                elif count[num] == candidates[name_str]:
                    comb[num].append(i)
                else:
                    pass

    for values in comb.values():
        for value in values:
            answer.append(''.join(value))
    answer.sort()
    return answer


'''
# Remind
1. defualtdict(int)
defualtdict는 해당 key가 없어도 +=1 연산이 가능하다. 해당 key를 만들어서 0으로 초기화해준 이후, +=1을 수행하여
1을 갖도록 만든다.
'''
# Other Solution


def solution(orders, courses):
    answer = []

    for course in courses:
        # 개수(course)에 맞는 조합을 모두 저장할 리스트다.
        array = []
        for order in orders:
            # order을 alphabetic order로 정렬한다.
            order = sorted(order)
            # 주어진 개수에 맞는 조합을 뽑아내고 array에 추가한다.
            array.extend(list(combinations(order, course)))

        # array에 중복된 원소들의 값들을 세어준다.
        count = Counter(array)

        if count:                                               # count에 원소가 존재하고
            if max(count.values()) >= 2:                        # 가장 많이 주문된 조합의 횟수가 2회 이상이라면
                for key, value in count.items():                # 모든 조합을 탐색하여
                    # 해당 조합의 주문 횟수가 최대 주문 횟수와 같다면
                    if value == max(count.values()):
                        # 반환할 리스트(answer)에 추가해준다.
                        answer.append("".join(key))

    return sorted(answer)
