# 시간 초과 O
from copy import deepcopy
import sys

def updateGrid(query, grid):
    min_value = sys.maxsize
    st_x, st_y, ed_x, ed_y = query
    # index값으로 보정
    st_x -= 1
    st_y -= 1
    ed_x -= 1
    ed_y -= 1
    
    #왼쪽 
    temp_1 = grid[st_x][st_y]
    min_value = min(min_value,temp_1)
    for i in range(st_x+1, ed_x+1):
        grid[i-1][st_y]= grid[i][st_y]
        min_value = min(min_value,grid[i-1][st_y])
        
    #위쪽
    temp_2 = grid[st_x][ed_y]
    min_value = min(min_value,temp_2)
    for i in range(ed_y-1, st_y, -1):
        grid[st_x][i+1] = grid[st_x][i]
        min_value = min(min_value,grid[st_x][i+1])
        
    grid[st_x][st_y+1]= temp_1
    
    #오른쪽
    temp_1 = grid[ed_x][ed_y]
    min_value = min(min_value,temp_1)
    for i in range(ed_x,st_x+1, -1):
        grid[i][ed_y] = grid[i-1][ed_y]
        min_value = min(min_value,grid[i][ed_y])
    grid[st_x+1][ed_y]= temp_2
    
    #아래쪽
    for i in range(st_y+1, ed_y):
        grid[ed_x][i-1] = grid[ed_x][i]
        min_value = min(min_value,grid[ed_x][i-1])
    grid[ed_x][ed_y-1] = temp_1
    return min_value, grid

def solution(rows, columns, queries):
    answer = []
    grid = [[(j)*columns + i + 1 for i in range(columns)]for j in range(rows)]
    for query in queries:
        min_val, update_grid = updateGrid(query, deepcopy(grid))
        answer.append(min_val)
        grid = deepcopy(update_grid)
    
    return answer

#시간 초과 X
from copy import deepcopy
import sys

def solution(rows, columns, queries):
    answer = []
    grid = [[(j)*columns + i + 1 for i in range(columns)]for j in range(rows)]
    for query in queries:
        min_value = sys.maxsize
        st_x, st_y, ed_x, ed_y = query
        # index값으로 보정
        st_x -= 1
        st_y -= 1
        ed_x -= 1
        ed_y -= 1

        #왼쪽 
        temp_1 = grid[st_x][st_y]
        min_value = min(min_value,temp_1)
        for i in range(st_x+1, ed_x+1):
            grid[i-1][st_y]= grid[i][st_y]
            min_value = min(min_value,grid[i-1][st_y])

        #위쪽
        temp_2 = grid[st_x][ed_y]
        min_value = min(min_value,temp_2)
        for i in range(ed_y-1, st_y, -1):
            grid[st_x][i+1] = grid[st_x][i]
            min_value = min(min_value,grid[st_x][i+1])

        grid[st_x][st_y+1]= temp_1

        #오른쪽
        temp_1 = grid[ed_x][ed_y]
        min_value = min(min_value,temp_1)
        for i in range(ed_x,st_x+1, -1):
            grid[i][ed_y] = grid[i-1][ed_y]
            min_value = min(min_value,grid[i][ed_y])
        grid[st_x+1][ed_y]= temp_2

        #아래쪽
        for i in range(st_y+1, ed_y):
            grid[ed_x][i-1] = grid[ed_x][i]
            min_value = min(min_value,grid[ed_x][i-1])
        grid[ed_x][ed_y-1] = temp_1
        answer.append(min_value)
    return answer
'''
# Remind
1. deepcopy를 많이쓰면 시간 초과 날 수 있다.
이에 함수를 사용하지 않고 def solution안에서 deepcopy를 사용하지 않고 해결.
2. 2차원 list에서 같은 열에 있는 원소를 slicing할 수는 없다.
이에 위의 과정에서 하나씩 swap해주는 형태로 해결
3. 간단하게 이동시킬 수 있는 방법이 있다.
위에서 나는 temp_1과 temp_2를 사용하여 복잡하게 회전시켰는데 왼쪽 세로 아래쪽 가로 오른쪽 세로 위쪽 가로
순으로 회전 시키면 temp를 한번써서 잘 회전시킬 수 있다. 더 생각해보면서 풀어보자.
'''