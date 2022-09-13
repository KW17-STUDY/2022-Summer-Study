#10분

n = int(input())

def check(extracted):
    num = int(''.join(extracted))
    root_num = int(num ** (1/2))
    for i in range(2,root_num+1):
        if num % i == 0:
            return False
    return True

def dfs(depth, extracted):
    if depth == n:
        print(''.join(extracted))
        return
    for i in range(1, 10):
        if depth == 0 and i == 1:
            continue
        extracted.append(str(i))
        if check(extracted):
            dfs(depth+1, extracted)
        extracted.pop()

dfs(0, [])

'''
1. root 구현 방법
num**(1/2) 사용!
2. for문 안에 21번 라인의 조건을 추가시킴으로써 가지치기!
'''