#1:00 ~ 2:10
import sys
from collections import deque

input = sys.stdin.readline

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x1, y1, x2, y2):
    return 0<= x1 <n and 0<=y1<m and\
        0<= x2 <n and 0<= y2 <m

def bfs(_1x, _1y, _2x, _2y):
    queue = deque([])
    queue.append([0, _1x, _1y, _2x, _2y])
    while queue:
        num ,_1x, _1y, _2x, _2y = queue.popleft()
        visited[_1x][_1y][_2x][_2y] = True
        if num >= 10:
            return -1
        #초기화
        for i in range(4):
            n_1x, n_1y = _1x+dxs[i], _1y+dys[i]
            n_2x, n_2y = _2x+dxs[i], _2y+dys[i]
            
            if in_range(n_1x, n_1y, n_2x, n_2y):
                if visited[n_1x][n_1y][n_2x][n_2y]:
                    continue
                if grid[n_1x][n_1y] =='#':
                    n_1x, n_1y = _1x, _1y
                if grid[n_2x][ n_2y] == '#':
                    n_2x, n_2y =_2x, _2y
                queue.append([num+1, n_1x, n_1y, n_2x, n_2y])
            elif 0 <= n_1x < n and 0 <= n_1y < m:  # coin2가 떨어진 경우
                return num + 1
            elif 0 <= n_2x < n and 0 <= n_2y < m:  # coin1가 떨어진 경우
                return num + 1
            else:  # 둘 다 빠진 경우 무시
                continue
    return -1

n, m = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(n)]
coins = []
visited = [[[[False for _ in range(m)] for _ in range(n)]for _ in range(m)]for _ in range(n)]


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'o':
            coins.append([i,j])

MIN = bfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1])
print(MIN)

'''
1. 19번 라인에서 num >= 10을 넣어야 한다.
num > 10일 때, return -1로 했는데 이렇게 하게되면
num이 10일 때, 32번 라인과 34번 라인에 의해서 11 return하게
되기 때문에 num >= 10으로 작성해야한다.
백준에서 60퍼센트 이상 차다가 틀렸었는데 이럴 때는 조건문에 잘 못 작성한게
없는지 찾아보자!
2. 배열로 작업하는 것 보다 직접 x1, y1, x2, y2를 작성해 주는 것이
속도면에서 빠르다!
3. 만약 경우의 수가 너무 많다면 visited를 사용해서 작업한다.
아래 처럼 4차원 배열을 이용한다.

visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[x1][y1][x2][y2] = True

Reference: https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-16197%EB%B2%88-%EB%91%90-%EB%8F%99%EC%A0%84-1-Python

4. 40번째 라인 return -1넣어야함.
queue 자체가 종료되었다는건 못찾았다는 의미!
'''