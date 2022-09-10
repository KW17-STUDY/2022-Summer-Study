#48
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
alphas = [ False for _ in range(26)]
x, y = 0, 0
max_move = 1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def in_range(x, y):
    return 0<=x<r and 0<=y<c
def can_go(x, y):
    if in_range(x,y) and not alphas[ord(grid[x][y])-65]:
        return True
    return False
def dfs(x, y, cnt):
    global max_move, alphas
    max_move = max(max_move, cnt)
    
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if  can_go(nx,ny):
            alphas[ord(grid[nx][ny])-65] = True
            dfs(nx, ny, cnt+1)
            alphas[ord(grid[nx][ny])-65] = False

alphas[ord(grid[x][y])-65] = True
dfs(x, y, 1)
print(max_move)

'''
아래 있는 코드들을 전부 pypy3로 제출함!

- alphas라는 visited를 사용해서 O(1)으로 풀어줬는데도 
시간초과 뜬 내 코드...
in 대신 O(1)을 통해서 해결하려고 했는데 실패햇다..

#48
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
alphas = [ False for _ in range(26)]
x, y = 0, 0
max_move = 1

def dfs(x, y, cnt):
    global max_move, alphas
    max_move = max(max_move, cnt)
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and not alphas[ord(grid[nx][ny])-65]:
            alphas[ord(grid[nx][ny])-65] = True
            dfs(nx, ny, cnt+1)
            alphas[ord(grid[nx][ny])-65] = False

alphas[ord(grid[x][y])-65] = True
dfs(x, y, 1)
print(max_move)

- zip말고 index를 통해서 nx와 ny를 계산한 코드
nx와 ny를 계산할 때 zip을 안사용하고 index를 통해서
해줬더니 시간초과 통과함..
속도: 7476ms
앞으로 시간이 중요할 떄는 
① zip을 사용하지 않고 index로 접근
② in말고 visited를 사용
제일 중요한건 zip안쓰고 index로 접근한다는게 제일중요!
zip을 사용해서 못푼거였음....

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
alphas = set()
x, y = 0, 0
max_move = 1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(x, y, cnt):
    global max_move, alphas
    max_move = max(max_move, cnt)
    
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0<=nx<r and 0<=ny<c and grid[nx][ny] not in alphas:
            alphas.add(grid[nx][ny])
            dfs(nx, ny, cnt+1)
            alphas.remove(grid[nx][ny])

alphas.add(grid[x][y])
dfs(x, y, 1)
print(max_move)

-visited를 사용하여 in 사용하지 않고 해결
속도: 5364
2000ms가까이 줄일 수 있었음

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
alphas = [ False for _ in range(26)]
x, y = 0, 0
max_move = 1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(x, y, cnt):
    global max_move, alphas
    max_move = max(max_move, cnt)
    
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0<=nx<r and 0<=ny<c and not alphas[ord(grid[nx][ny])-65]:
            alphas[ord(grid[nx][ny])-65] = True
            dfs(nx, ny, cnt+1)
            alphas[ord(grid[nx][ny])-65] = False

alphas[ord(grid[x][y])-65] = True
dfs(x, y, 1)
print(max_move)


- 함수화 시키면 시간이 조금 늘어나긴함!
속도: 5856ms

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
alphas = [ False for _ in range(26)]
x, y = 0, 0
max_move = 1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def in_range(x, y):
    return 0<=x<r and 0<=y<c
def can_go(x, y):
    if in_range(x,y) and not alphas[ord(grid[x][y])-65]:
        return True
    return False
def dfs(x, y, cnt):
    global max_move, alphas
    max_move = max(max_move, cnt)
    
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if  can_go(nx,ny):
            alphas[ord(grid[nx][ny])-65] = True
            dfs(nx, ny, cnt+1)
            alphas[ord(grid[nx][ny])-65] = False

alphas[ord(grid[x][y])-65] = True
dfs(x, y, 1)
print(max_move)
'''
'''
Remind
1. python 'in' 시간 복잡도:
set, dict에서는 평균:O(1) worst:O(N)
list, tuple에서는 평균:O(N)
'''
