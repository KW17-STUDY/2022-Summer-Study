# 내 답
from collections import deque
import sys

input = sys.stdin.readline

node_num, edge_num = map(int, input().split())
indegree = [0 for _ in range(node_num + 1)]
grid = [[]for _ in range(node_num+1)]
order = []

for i in range(edge_num):
    start, end = map(int, input().split())
    grid[start].append(end)
    indegree[end] += 1
'''
q = deque()
for idx, i in enumerate(indegree):
    if idx == 0:
        continue
    if i == 0:
        q.append(idx)
        order.append(idx)

while q:
    v = q.popleft()
    for i in grid[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            order.append(i)
            print(i)

print(order)
'''
# 답안


def topology_sort():
    result = []
    q = deque()

    # 초기에 진입차수가 0인 것으로 q초기화
    for i in range(1, node_num+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 방문처리
        result.append(now)
        for i in grid[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
'''
# Remind
1. queue를 사용할 때, 출력하거나 그 값을 저장해야한다면 popleft해서 가져오고, 바로 append하거나 print해서 방문처리한다.
2. 진입 차수 초기화 할 때, for i in degree를 하게되면 0번째 index까지 가져오게 되므로 range를 통해 (1, node_num+1) 사용해서
가져오는 것이 깔끔한 것 같다.
'''
