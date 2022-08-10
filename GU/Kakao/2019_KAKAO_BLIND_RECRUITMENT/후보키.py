from itertools import combinations
from collections import defaultdict

# comb의 부분 집합이 candi에 있는지 확인
def check(candi, comb):
    for key in candi:
        for i in combinations(comb, len(key)):
            if key == i:
                return False
    return True
    
def solution(relation):
    cols = len(relation[0])
    candidate_keys = []
    keys = defaultdict(lambda : defaultdict(int)) # defulatdict안에 defaultdict 선언
    for i in range(1, cols+1):
        for comb in combinations(list(range(cols)),i): # list(range(cols)) 를 list(range(4))라고 해서 에러 못잡았다...
            for row in relation:
                key = []
                for j in comb:
                    key.append(row[j])
                key = ''.join(key)
                keys[comb][key] += 1

    for comb_key in keys:
        success = True
        for cnt in keys[comb_key].values():
            if cnt != 1:
                success = False
                break
        if success and check(candidate_keys, comb_key):
            candidate_keys.append(comb_key)

    return len(candidate_keys)

'''
# Remind
1. 알고리즘에서 상수를 이용하지 말고 변수이용하기
상수를 이용해서 에러가 생겼다... 조심하자
2. keys = defaultdict(lambda : defaultdict(int))
'''


