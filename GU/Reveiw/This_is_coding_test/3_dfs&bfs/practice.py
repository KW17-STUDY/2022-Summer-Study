import sys
from copy import copy


'''
# 전역변수를 parameter로 넘겼을 때, 전역변수 자체가 수정되는지 확인

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [
    [] for _ in range(n+1)
]
answer = 0
visited = [False for _ in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    grid[start].append(end)
    grid[end].append(start)


def dfs(v):
    global answer
    visited[v] = True
    for i in grid[v]:
        if not visited[i]:
            answer += 1
            dfs(i)


def another_dfs(visited, v, grid):
    visited = copy(visited)
    visited[v] = True
    print(visited)


dfs(1)
visited = [False for _ in range(n+1)]
another_dfs(visited, 1, grid)
print(visited)
'''

print(not False)
print(not 0)
print(not 1)
print(not -1)
print(not 100)

x = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
x.sort(key=lambda x: (x[1], x[0]))
print(x)
