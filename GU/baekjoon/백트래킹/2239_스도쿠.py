#50
import sys
input = sys.stdin.readline
grid = [list(map(int, input().rstrip())) for _ in range(9)]
have_to_solve = []

for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            have_to_solve.append((i,j))
zeros = len(have_to_solve)

def checkCol(y, num):
    for i in range(9):
        if grid[i][y] == num:
            return False
    return True

def checkRow(x, num):
    for i in range(9):
        if grid[x][i] == num:
            return False
    return True

def checkBox(x, y, num):
    x, y = x//3*3, y//3*3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if grid[i][j] == num:
                return False
    return True
def printGrid():
    for i in range(9):
        print(''.join(map(str,grid[i])))

def dfs(depth):
    if depth == zeros:
        printGrid()
        exit()

    x, y = have_to_solve[depth][0], have_to_solve[depth][1] 
    for i in range(1,10):
        if checkCol(y, i) and checkRow(x, i) and checkBox(x, y, i):
            grid[x][y] = i
            dfs(depth + 1)
            grid[x][y] = 0
dfs(0)
'''
#Remind
1. 46번 라인 꼭 들어가야함!
check()에서 반영되기 때문에...!!!
처음에 안들어가도 된다고 생각해서 안해줬었는데 꼭 넣어야한다!!
'''