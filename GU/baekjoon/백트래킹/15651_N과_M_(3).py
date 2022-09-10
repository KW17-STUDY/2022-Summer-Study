#product 구현
n, m = map(int, input().split())

def printAnswer(extracted):
    for i in extracted:
        print(i, end = ' ')
    print()

def dfs(depth, extracted):
    if depth == m:
        printAnswer(extracted)
        return
    for i in range(1, n+1):
        extracted.append(i)
        dfs(depth+1, extracted)
        extracted.pop()

dfs(0, [])

from itertools import product
print(list(product([i for i in range(1,5)], repeat=2)))