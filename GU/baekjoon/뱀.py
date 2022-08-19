#8:20~8:18
from collections import deque

n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]
app_cnt = int(input())
for _ in range(app_cnt):
    app_r, app_c = map(int,input().split())
    grid[app_r-1][app_c-1] = 1
dir_convert_cnt = int(input())
dir_list = []
for _ in range(dir_convert_cnt):
    sec, dir = input().split()
    dir_list.append((int(sec), dir))


def in_range(nx, ny):
    return nx>=0 and ny>=0 and nx<n and ny<n

def printGrid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end = '     ')
        print()

head, tail = [0,0], [0,0]
tail_list=deque([tail])
grid[0][0] = -1
dxs, dys = [0,1,0,-1],[1,0,-1,0]#동 남 서 북
dir = 0
time = 0
while True:
    # 시간 경과
    time += 1
    #print('현재 시간:', time)
    # 정해진 방향에 벽이나 자신의 몸이 있는지 확인
    new_head_x = head[0] + dxs[dir]
    new_head_y = head[1] + dys[dir]
    #print('방향:', dir)
    #print(new_head_x, new_head_y)
    #print(in_range(new_head_x, new_head_y))
    if not in_range(new_head_x, new_head_y) or grid[new_head_x][new_head_y] == -1:
        #print('exit')
        #게임 종료
        break
    elif grid[new_head_x][new_head_y] == 1: #사과가 있다면
        grid[new_head_x][new_head_y] = -1
        head = [new_head_x, new_head_y]
        tail_list.append(head)
    else: #아무것도 없다면
        grid[new_head_x][new_head_y] = -1
        head = [new_head_x, new_head_y]
        tail_list.append(head)

        #tail 조정
        (t_x, t_y) = tail_list.popleft() #tail list에서 없애기
        grid[t_x][t_y] = 0 #tail을 grid 상에서 없애기

    
    # 시간에 따른 방향 변경
    for (sec, direction) in dir_list:
        if time == sec:
            if direction == 'L':#왼쪽
                dir -= 1
            if direction == 'D':
                dir += 1
            dir %= 4
            dir_list.remove((sec, direction))
    #printGrid()
print(time)

