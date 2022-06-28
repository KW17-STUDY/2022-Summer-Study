# bfs
from collections import deque

n, m, k, x = tuple(map(int, input().split()))
graph = [
    [] for _ in range(n+1)
]
distances = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    start, end = tuple(map(int, input().split()))
    graph[start].append(end)


def bfs(x):
    queue = deque([x])
    distances[x] = 0
    visited[x] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                distances[i] = distances[v] + 1
                visited[i] = True


bfs(x)
print(distances)
print(visited)
check = False
for idx, i in enumerate(distances):
    if i == k:
        print(idx, end=' ')
        check = True

if not check:
    print(-1)

'''
# Remind
1. False 와 0을 not하면 True가 나온다. 이외의 -1, 100, True 등등은 not 연산시 False가 나오게 된다.
이에 distance에 0과 False를 동시에 넣고 not distance하면 원하는 방향으로 동작하지 않을 수 있으므로
visited와 distance로 기능을 나누었다.

'''
