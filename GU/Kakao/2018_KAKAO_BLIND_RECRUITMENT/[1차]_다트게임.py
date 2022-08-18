#30분

import re

def solution(dartResult):
    step = 0
    step_point = []
    steps = re.findall('[0-9]+[SDT]+[*#]*', dartResult)
    
    for idx, step in enumerate(steps):
        num = re.match('[0-9]+',step)[0]
        operator = re.search('([^0-9]+)', step).group(0)
        steps[idx] = [num, operator]
    
    """
    for i in range(len(steps)):
        j = 0
        tmp = ''
        while steps[i][j].isdigit():
            tmp+=steps[i][j]
            j+=1
        steps[i] = [int(tmp), steps[i].replace(tmp,"")]
    """
    for idx, (num, operator) in enumerate(steps):
        num = int(num)
        for op in operator:
            if op == 'D':
                num = num ** 2
            elif op == 'T':
                num = num ** 3
            elif op == '*':
                num*=2
                if idx != 0:
                    step_point[idx-1]*=2
            elif op == '#':
                num*=-1 
        step_point.append(num)
    return sum(step_point)

#다른 사람 코드
def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)

'''
#Remind
1. 하나하나씩 입력을 받으면서 숫자라면 이어붙히고
SDT라면 제곱 연산 이후 step별 결과를 score라는 리스트에 저장한다.
*이나 #이라면 score의 리스트에 존재하는 최근 값들을 수정한다.
'''


