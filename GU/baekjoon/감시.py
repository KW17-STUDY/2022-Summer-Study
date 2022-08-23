from copy import deepcopy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
#cctv 감시 방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}
INF = sys.maxsize
min_value = INF
def copy(list1, list2):
    for i in range(n):
        for j in range(m):
            list2[i][j] = list1[i][j]
def countZeros(grid):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                cnt += 1
    return cnt
def in_range(x, y):
    return 0<=x<n and 0<=y<m
def move(x, y, d, tmp):
    nx, ny = x+dxs[d] , y+dys[d]
    while in_range(nx+dxs[d], ny+dys[d]) and tmp[nx][ny] != 6:
        if tmp[nx][ny] == 0:
            tmp[nx][ny] = '#'
        nx, ny = nx+dxs[d] , ny+dys[d]
    if in_range(nx, ny) and tmp[nx][ny] != 6:
        if tmp[nx][ny] == 0:
            tmp[nx][ny] = '#'
        
def printGrid(grid):
    print('------------')
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end=' ')
        print()
def dfs(depth, grid):
    global min_value 
    #해당 depth 안에서 grid로 복원시켜야할일이 있기 때문에
    #tmp에 grid 저장
    tmp = [[0 for _ in range(m)]for _ in range(n)]
    copy(grid, tmp)
    #tmp = deepcopy(grid)
    
    if len(cctv) == depth:
        value = countZeros(grid)
        min_value = min(min_value, value)
        return
    x, y, dir = cctv[depth]
    # 방향대로 색칠 하기
    for dirs in direction[dir]:
        for d in dirs:
            move(x,y, d, tmp)
        dfs(depth+1, tmp)
        copy(grid, tmp)

        #tmp = deepcopy(grid)


cctv = []
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0 and grid[i][j] != 6:
            cctv.append((i,j,grid[i][j]))
dfs(0, grid)
print(min_value)

'''
#Remind
1. dict를 사용하면 편리할 수 있다.
if문을 사용하기 보다는 dict를 사용해서 간결하게 만들 수 있다.

2. 일반화를 잘하자.
1->[0,1,2,3]
2>[[0,2],[1,3]]
1번은 한 step당 0, 1, 2, 3을 각각 하나씩 해야하므로
1을 [[0],[1],[2],[3]]으로 사용해야한다.
'''
'''
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
3. 풀이 방법
cctv에 대한 정보들을 cctv list에 담아 놓고 dfs의 depth를 이용하여 cctv list에 순차적으로 접근한다.
이 때, 알맞게 grid에 대한 정보를 저장해주어 복원시키기 위해 tmp를 사용한다.
'''