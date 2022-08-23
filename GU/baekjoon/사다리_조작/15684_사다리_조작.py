#30
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline
n, m, h = map(int, input().split())
grid = [[False for _ in range(n+1)] for _ in range(h+1)]
info = []

def getResult(grid, num):
    for i in range(1,len(grid)):
        if grid[i][num] == True:
            num = num+1
        elif grid[i][num-1] == True:
            num = num-1
    return num
    
def checkResult(grid):
    for i in range(1,len(grid[0])):
        if getResult(grid, i) != i:
            break
    else:
        return True
    return False

def printGrid(grid):
    for i in range(h+1):
        for j in range(n+1):
            print(grid[i][j], end = ' ')
        print()

def checkComb(comb):
    global info
    tmp = []
    for rows in comb:
        flag = True
        for row in rows:
            if row[1] >= len(grid[0])-1:
                flag = False
            for i in info:
                if row[0] == i[0]:
                    if abs(row[1]-i[1]) == 1:
                        flag = False
        if flag == True:
            tmp.append(rows)
    return tmp
    
def operate(grid):
    answer = None
    for i in range(4):
        comb = combinations(candi,i)
        comb = checkComb(comb)
        for rows in comb:
            for row in rows:
                grid[row[0]][row[1]] = True
            if checkResult(grid):
                answer = i
                return answer
            for row in rows:
                grid[row[0]][row[1]] = False
    if answer == None:
        answer = -1
    return answer

for i in range(m):
    #a, b => b와 b+1번 세로선을 a번 점선 위치에 연결
    a, b = map(int,input().split())
    info.append([a,b])
    grid[a][b] = True
#조합할 후보들 설정
candi = []
for i in range(1, len(grid)):
    for j in range(1,len(grid[0])):
        if grid[i][j] == False:
            candi.append([i,j])
#bruteforce
#1개부터 3개까지 골라서 생성
answer = operate(grid)
print(answer)
