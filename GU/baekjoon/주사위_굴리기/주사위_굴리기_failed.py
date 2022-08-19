#36 42
#32 27

n,m,x,y,k = map(int,input().split())
grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))
order = list(map(int,input().split()))
order = [i-1 for i in order]
up_down = [0 for _ in range(4)] #윗면, 아래, 바닥, 위
#아래로 가면 윗면이 위가됨
# 아래로가면 -1해주면됨.(1이 윗면이였었을 때 2가 위, 5가 바닥)
# 제일 윗면과 아랫면을 가리키는 포인터를 1씩 뺴주면됨.
left_right = [0 for _ in range(4)]#윗면, 오른, 바닥, 왼
u_up_side, u_down_side = 0,2
l_up_side, l_down_side = 0,2
dxs, dys = [0,0,-1,1], [1,-1,0,0]

def in_range(x, y):
    return x>=0 and y>=0 and x<n and y<m 

def printGrid():
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end=' ')
        print()
for dir in order:
    #이동 가능 여부 체크
    nx, ny = x+dxs[dir], y+dys[dir]
    if not in_range(nx, ny):
        continue
    #이동 가능하다면 이동
    else:
        x, y = nx, ny

    if dir == 0:#동
        #updown 에서 가리키는 포인터 수정
        l_up_side = (l_up_side-1)%4
        l_down_side = (l_down_side-1)%4

        #가로로 존재하는 부분 변경
        up_down[u_up_side] = left_right[l_up_side]
        up_down[u_down_side] = left_right[u_down_side]
        
    if dir == 1:
        #updown 에서 가리키는 포인터 수정
        l_up_side = (l_up_side+1)%4
        l_down_side = (l_down_side+1)%4
        #가로로 존재하는 부분 변경
        up_down[u_up_side] = left_right[l_up_side]
        up_down[u_down_side] = left_right[u_down_side]

    if dir == 2:#북
        #updown 에서 가리키는 포인터 수정
        u_up_side = (u_up_side+1)%4
        u_down_side = (u_down_side+1)%4

        #가로로 존재하는 부분 변경
        left_right[l_up_side] = up_down[u_up_side]
        left_right[l_down_side] = up_down[u_down_side]

    if dir == 3:#남
        #updown 에서 가리키는 포인터 수정
        u_up_side = (u_up_side-1)%4
        u_down_side = (u_down_side-1)%4
        #가로로 존재하는 부분 변경
        left_right[l_up_side] = up_down[u_up_side]
        left_right[l_down_side] = up_down[u_down_side]

    # 지도 및 주사위 수정
    if grid[x][y] == 0:
        grid[x][y] = up_down[u_down_side] 
    else:
        up_down[u_down_side] = grid[x][y]
        left_right[l_down_side] = grid[x][y]
        grid[x][y] = 0
    
    print(up_down[u_up_side] )
