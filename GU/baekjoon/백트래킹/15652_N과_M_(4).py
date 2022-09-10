#combinations with replacement 구현
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
        #combinations에서는 dfs에 i+1을 넣었었다.
        #그것만 다름!
        dfs(depth+1, i, extracted)
        extracted.pop()
dfs(0, 1, [])

from itertools import combinations_with_replacement
print(list(combinations_with_replacement([i for i in range(1,n+1)], 2)))