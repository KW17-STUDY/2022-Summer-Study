INF = int(1e9)

# 노드 갯수
n = int(input())
# 마을 갯수
m = int(input())

# graph 초기화
graph = [[INF for _ in range(n+1)]for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0


for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = cost

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print()
