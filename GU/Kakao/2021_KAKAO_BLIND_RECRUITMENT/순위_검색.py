from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for inf in info:
        words = inf.split()
        for num in range(5):
            for comb in combinations(words[:-1], num):
                key, value = ''.join(comb), int(words[-1])
                info_dict[key].append(value)

    for key in info_dict:
        info_dict[key] = sorted(info_dict[key])
        
    for question in query:
        words = question.split()
        filtered_words = []
        for word in words:
            if word == 'and' or word =='-':
                continue
            filtered_words.append(word)
        key, value = ''.join(filtered_words[:-1]), int(filtered_words[-1])
        cnt = len(info_dict[key]) - bisect_left(info_dict[key],value)
        answer.append(cnt)
            
    return answer
'''
#Remind
1. 이진 탐색을 쉽게 구현할 수 있는 bisect 알아두기.
github에 까먹지 않도록 정리

2. 효율성 해결 방법 
info list 길이: 50,000
query list 길이: 100,000
생각업이 짜게되어 5,000,000,000 연산이 이루어지게 된다.
이에 시간초과가 나게 되서 위와 같이 구현한다.
info list안의 데이터들을 0~4개만큼 뽑아서(combination) 점수를 value로 하는 hash를 만든다.
이후, query list에 존재하는 query문 하나하나를 가져와서 hash함수의 key에 맞는 형태로 변환 후,
숫자를 세어준다.
이때도 시간초과를 고려해서 log n 만큼 걸리는 이진탐색(bisect library)을 사용한다.
'''