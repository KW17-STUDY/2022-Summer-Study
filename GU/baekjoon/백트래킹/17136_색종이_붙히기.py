#1시간 8분
import sys

input = sys.stdin.readline
grid = [list(map(int,input().rstrip().split())) for _ in range(10)]
paper = [[0 for _ in range(10)] for _ in range(10)]
ones = []
MIN_PAP = 9999
remain_papers = [5 for _ in range(6)]

for i in range(10):
    for j in range(10):
        if grid[i][j] == 1:
            ones.append((i, j))
def in_range(x, y, size):
    return 0<=x+size-1<=9 and 0<=y+size-1<=9

def check_valid(x, y, size):
    if not in_range(x, y, size):
        return False

    for i in range(size):
        for j in range(size):
            # 1이 아니거나 색종이가 붙여져 있을 때 False
            if grid[x+i][y+j] == 0 or paper[x+i][y+j] == 1:
                return False
    return True

def check_paper(x, y, size):
    global paper
    for i in range(size):
        for j in range(size):
            paper[x+i][y+j] = 1
    return 

def remove_paper(x, y, size):
    global paper
    for i in range(size):
        for j in range(size):
            paper[x+i][y+j] = 0
    return 
def printGrid(paper):
    for i in range(10):
        for j in range(10):
            print(paper[i][j], end= ' ')
        print()

def dfs(depth, cnt):
    global MIN_PAP

    if depth == len(ones):
        MIN_PAP = min(MIN_PAP, cnt)
        return

    if sum([remain_papers[i] for i in range(1,6)]) == 0:
        return

    x, y = ones[depth][0], ones[depth][1]
    if paper[x][y] == 1:
        dfs(depth+1, cnt)
    else:
        for i in range(5,0,-1):
            if remain_papers[i] > 0 and check_valid(x, y, i):
                check_paper(x, y, i)
                remain_papers[i] -= 1
                dfs(depth+1, cnt+1)
                remove_paper(x, y, i)
                remain_papers[i] += 1


dfs(0, 0)
if MIN_PAP == 9999:
    print(-1)
else:
    print(MIN_PAP)

'''
1. back tracking에서 조건에 따라 아예 재귀 밖으로 나갈지 아니면 새로운 재귀를 시작할지를 잘 결정해주자.
조건문에 따라 알맞은 흐름으로 코딩하기.
남아있는 paper가 없으면 -> 재귀를 나가기.
이미 색종이를 붙힌 곳이면 -> 다음 재귀로
아직 붙혀지지 않는 곳이면 -> 맞는 색종이 붙히고 나서 다음 재귀로!
'''