#47분
#극이 다르면 반대방향
#N극 0 S극 1
from copy import deepcopy


def turn(info):
    temp = [None for _ in range(len(info))]
    temp[0]= info[-1]
    temp[1:] = info[:-1]
    return temp[:]

def reverse_turn(info):
    temp = [None for _ in range(len(info))]
    temp[-1] = info[0]
    temp[:-1] = info[1:]
    return temp[:]

def recursive_turn(temp_status, num, dir, visited, is_turn):
    global n

    if visited[num] or is_turn==False:
        return
    else: 
        visited[num] = True
        
    temp_status[num] = turn(temp_status[num]) if dir == 1 else reverse_turn(temp_status[num])
    #왼족
    if num-1>=0:
        #돌려야할 때
        if status[num][6] != status[num-1][2]:
            if dir ==1:
                recursive_turn(temp_status,num-1,-1, visited, True)
            else:
                recursive_turn(temp_status,num-1,1, visited, True)
    if num+1<n:
        if status[num][2] != status[num+1][6]:
            if dir ==1:
                recursive_turn(temp_status,num+1,-1, visited, True)
            else:
                recursive_turn(temp_status,num+1,1, visited, True)
    
n = 4
status = [list(input()) for _ in range(n)]
turn_cnt = int(input())
for _ in range(turn_cnt):
    visited = [False for _ in range(n)]
    temp_status = deepcopy(status)
    # 톱니바퀴 번호, 방향(시계:1 반시계:-1)
    (num, dir) = map(int,input().split())
    #반시계일 때
    recursive_turn(temp_status, num-1, dir, visited, True)
    status = temp_status

score = 0
for i in range(n):
    if status[i][0] == '0':
        pass
    else:
        score += 2**i
print(score)

