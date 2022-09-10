# 7분
# combinations 구현 
n, m = map(int, input().split())

def printAnswer(extracted):
    for i in extracted:
        print(i, end = ' ')
    print()

def dfs(depth, start, extracted):
    if depth == m:
        printAnswer(extracted)
        return
    for i in range(start, n+1):
        extracted.append(i)
        # i+1을 dfs에 넣어주는게 핵심!
        # 실수로 start를 넘겨줘서 틀렸었음!
        dfs(depth+1, i+1, extracted)
        extracted.pop()

dfs(0, 1, [])

# 입력이 4, 2인 경우
from itertools import combinations
print(list(combinations([i for i in range(1,5)], 2)))