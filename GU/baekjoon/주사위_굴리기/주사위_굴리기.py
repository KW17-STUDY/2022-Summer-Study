#1시간
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
        #가로 수정
        new_left_right = [0*4]
        new_left_right[0] = left_right[-1]
        new_left_right[1:] = left_right[:-1]
        left_right = new_left_right[:]
        
        #세로 수정
        up_down[0] = left_right[0]
        up_down[2] = left_right[2]

    if dir == 1:
        #가로 수정
        new_left_right = [0*4]
        new_left_right[-1] = left_right[0]
        new_left_right[:-1] = left_right[1:]
        left_right = new_left_right[:]
        
        #세로 수정
        up_down[0] = left_right[0]
        up_down[2] = left_right[2]
        

    if dir == 2:#북
        #updown 수정
        new_up_down = [0*4]
        new_up_down[-1] = up_down[0]
        new_up_down[:-1] = up_down[1:]        
        up_down = new_up_down[:]

        #가로 수정
        left_right[0] = up_down[0]
        left_right[2] = up_down[2]

    if dir == 3:#남
        #updown 수정
        new_up_down = [0*4]
        new_up_down[0] = up_down[-1]
        new_up_down[1:] = up_down[:-1]        
        up_down = new_up_down[:]

        #가로 수정
        left_right[0] = up_down[0]
        left_right[2] = up_down[2]

    # 지도 및 주사위 수정
    if grid[x][y] == 0:
        grid[x][y] = up_down[2]
    else:
        up_down[2] = grid[x][y]
        left_right[2] = grid[x][y]
        grid[x][y] = 0
    
    print(left_right[0])

#문제 제대로 읽자....
#grid[x][y] = 0 이거 안넣어줬다..
'''
#Remind
1. 가리키는 개념으로 푸려고 했는데 헷갈림.
변수이름도 많고 그래서..
이에 0번째 index와 2번째 index가 각각 맨위, 맨 아래를 의미하는 list를 선언해서 사용
'''
