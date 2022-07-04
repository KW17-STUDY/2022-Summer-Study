import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((end_node, cost))
distance = [INF for _ in range(n+1)]


def dijkstra(start):
    q = []
    # cost, node
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for idx, i in enumerate(distance):
    if idx == 0:
        continue
    print('{}: {}'.format(idx, i))

print(INF)

'''
# Remind
1. Time complexity: O(Elog(V))
우선 순위 큐에서 삽입 삭제는 log(N)시간 만큼 걸리게 되는데 E개의 간선을 넣고 빼어 Elog(E)가 걸리게 된다.
이 때, 모든 간선이 서로 연결되어 있다면 (V-1)^2이 되는데 이를 고려해서 정리하게 되면 Elog(V)만큼 걸리게 된다.
2. INF 라는 변수를 사용해서 초기화
INF = 1e9
3. 우선 순위 큐를 구현하기 위해 min heap(최소 heap)을 사용하였다.
min heap은 tree 자료구조에 속한다.
'''
