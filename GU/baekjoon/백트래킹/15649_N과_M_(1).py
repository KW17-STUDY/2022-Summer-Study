#10분
#permutations
#parameter로 넘겨서 풀기
def printAnswer(extracted):
    for i in extracted:
        print(i, end = ' ')
    print()

n, m = map(int,input().split())
def dfs(depth, extracted):
    if depth == m:
        printAnswer(extracted)
        return

    for i in range(1, n+1):
        # extracted에 없는 경우에만 넣어주면 됨
        if i not in extracted:
            extracted.append(i)
            dfs(depth+1, extracted)
            extracted.pop()
dfs(0, [])

from itertools import permutations
print(list(permutations([i for i in range(1,5)], 2)))
'''
# 전역변수로 풀기
def printAnswer(extracted):
    for i in extracted:
        print(i, end = ' ')
    print()

n, m = map(int,input().split())
extracted = []
def dfs(depth):
    global extracted 

    if depth == m:
        printAnswer(extracted)
        return

    for i in range(1, n+1):
        if i not in extracted:
            extracted.append(i)
            dfs(depth+1)
            extracted.pop()
dfs(0)
'''
