#5
import sys
input = sys.stdin.readline
grid = [list(map(int,input().split())) for _ in range(9)]
have_to_solve_list = []
have_to_solve = 0
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            have_to_solve += 1
            have_to_solve_list.append([i,j])

def checkrow(col, k):
    for i in range(9):
        if grid[i][col] == k:
            return False
    return True

def checkcol(row,k):
    for i in range(9):
        if grid[row][i] == k:
            return False
    return True

def checkbox(row, col, k):
    row_start, col_start = int(row//3), int(col//3)
    for i in range(row_start*3, row_start*3+3):
        for j in range(col_start*3, col_start*3+3):
            if grid[i][j] == k:
                return False
    return True
    

def dfs(depth):
    global grid, cnt
    if depth == have_to_solve:
        printGrid(grid)
        exit(0)

    i, j = have_to_solve_list[depth][0], have_to_solve_list[depth][1]
    for k in range(1, 10):
        if checkrow(j, k) and checkcol(i,k) and checkbox(i,j,k):
            grid[i][j] = k
            dfs(depth+1)
            grid[i][j] = 0

def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end= ' ')
        print()
dfs(0)
'''
# Remind
1. dfs 부분에서 아래 부분이 인상적이였다.
    i, j = have_to_solve_list[depth][0], have_to_solve_list[depth][1]
    for k in range(1, 10):
        if checkrow(j, k) and checkcol(i,k) and checkbox(i,j,k):
            grid[i][j] = k
            dfs(depth+1)
            grid[i][j] = 0
나는 아래와 같이 구현함.
    for i,j in have_to_solve_list:
        if grid[i][j] == 0:
            for k in range(1, 10):
                if checkrow(j, k) and checkcol(i,k) and checkbox(i,j,k):
                    grid[i][j] = k
                    dfs(depth+1)
                    grid[i][j] = 0
내꺼 같이 구현하게 되면 depth가 0일 때, have_to_solve_list에 있는 
바꿔야하는 모든 위치들을 한번씩 다 바꿔주기 때문에 너무 오래걸림.
변견된 코드에서는 depth별로 담당하는 바꿔야하는 부분을 56번째 라인을 
통해서 설정시켜주고 여기에 1부터 10까지 넣어가면서 다음 depth로 이동!
위의 코드 배우기.

2. sys.exit(0)을 사용하면 바로 종료 가능!

3. for i in range(1, 10)을 사용해서 1~9까지 돌려야하는데
실수로 for i in rang(1,9)를 사용해서 1~8까지 돌려버림..
정신차리자!

4. zero인 것들을 싹 뽑아서 have_to_solve_list에 넣고,
depth에 따라 한 좌표만 처리하도록 have_to_solve_list[depth]를
사용.
'''