#1시간 30분...
from itertools import permutations
import sys
from copy import deepcopy

input = sys.stdin.readline
n, m, oper_num = map(int,input().rstrip().split())
origin_grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
operations = [tuple(map(int, input().rstrip().split())) for _ in range(oper_num)]
def printGrid():
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end = ' ')
        print()
def rotate(x, y, diff):
    global grid
    for i in range(1, diff+1):
        
        # 아래
        temp = grid[x+i][y-i]
        grid[x+i][y-i:y+i]= grid[x+i][y-i+1:y+i+1]
        
    
        #오른쪽
        for j in range(x+i-1, x-i-1,-1):
            grid[j+1][y+i]= grid[j][y+i]
        
        
        #위쪽
        grid[x-i][y-i+1:y+i+1]= grid[x-i][y-i:y+i]
        #왼쪽
        for j in range(x-i+1, x+i):
            grid[j-1][y-i] = grid[j][y-i]

        grid[x+i-1][y-i]= temp
        
INF = sys.maxsize
MIN_VAL = INF

for order in permutations(operations, len(operations)):
    grid = deepcopy(origin_grid)
    
    for operation in order:
        x, y, diff = operation
        rotate(x-1, y-1, diff)
    MIN_VAL = min(MIN_VAL, min(list(sum(i) for i in grid)))

print(MIN_VAL)

'''
1. 다른 사람 코드
from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
RCS = [list(map(int, input().split())) for _ in range(K)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = 1e9

for perm in permutations(RCS,K):
    temp = deepcopy(A)
    for r, c, s in perm:
        for i in range(0, s):
        top = [r-s+i-1, c-s+i-1]
        bottom = [r+s-i-1, c+s-i-1]
        nx, ny = top
        tmp = temp[nx][ny]

        for i in range(4):
            while True:
                nx = nx + dx[i]
                ny = ny + dy[i]
                if not (nx >= top[0] and nx <= bottom[0] and ny >= top[1] and ny <= bottom[1]):
                    nx = nx - dx[i]
                    ny = ny - dy[i]
                    break
                tmp, temp[nx][ny] = temp[nx][ny], tmp

    for row in temp:
        res = min(res, sum(row))
    print(res)

※ 한 grid 씩, rotation 하는 부분
for i in range(4):
    while True:
        nx = nx + dx[i]
        ny = ny + dy[i]
        if not (nx >= top[0] and nx <= bottom[0] and ny >= top[1] and ny <= bottom[1]):
            nx = nx - dx[i]
            ny = ny - dy[i]
            break
        tmp, temp[nx][ny] = temp[nx][ny], tmp

2. 90도 회전 코드
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
엔마일마알로 위우기!

Reference
1. 한 grid씩 회전: https://dev-dain.tistory.com/154
2. 90도씩 회전: https://shoark7.github.io/programming/algorithm/rotate-2d-array
'''