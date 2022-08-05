import sys

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    grid = [[INF for _ in range(n+1)]for _ in range(n+1)]
    for i in range(1, n+1):
        grid[i][i] = 0
        
    for start, end, cost in fares:
        grid[start][end] = cost
        grid[end][start] = cost
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j] = min(grid[i][k]+grid[k][j], grid[i][j])
                
    min_cost = INF
    for i in range(1, n+1):
        min_cost = min(min_cost, grid[s][i]+grid[i][a]+grid[i][b])
        
    return min_cost

"""
#Remind
1. floyd warshall알고리즘에서 중간에 거쳐가는 k에 대한 for문을 먼저 넣어야한다.
"""