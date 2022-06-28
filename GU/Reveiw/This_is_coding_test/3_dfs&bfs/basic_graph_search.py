import sys


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


dfs(1)
print(answer)

'''
# Remind
1. 전역 변수를 parameter로 넣어 사용하게되면 값 자체가 들어오는 것이 아니기 때문에 
함수안에서 해당 parameter의 값을 변경하게 되면 실질적으로 전역변수의 값을 변경하는 것이다.
이에 함수안에서 parameter를 수정하게 되면 전역 변수의 값이 바뀌게 되어 조심해야한다.
이에 이중 리스트의 경우, deepcopy를 사용해서 그 값만 취한다.
'''
