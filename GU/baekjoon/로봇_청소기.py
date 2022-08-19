#28

n, m = map(int,input().split())
x, y, dir = map(int,input().split())
#dir: 0북 1 동, 2남,3서
grid = [list(map(int,input().split())) for _ in range(n)]
dxs, dys = [-1,0,1,0],[0,1,0,-1]
answer = 0

def printGrid():
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end = ' ')
        print()

def can_go(x, y):
    if grid[x][y] == 0:
        return True
    return False

grid[x][y] = -1
answer+=1
while True:
    # 방향 회전하기
    for _ in range(4):
        dir = (dir-1)%4
        dx, dy = dxs[dir], dys[dir]
        nx, ny = x+dx, y+dy
        if can_go(nx, ny):
            answer += 1
            x, y = nx, ny
            grid[x][y] = -1
            break
    else:
        nx, ny = x-dxs[dir], y-dys[dir]
        if grid[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
        


print(answer)

'''
1. 31행과 32행 바꿔써서 시간 엄청 들었음.. 
이런 실수를 줄이자...
또한 문제 이해를 잘 못해서 자꾸 dfs로 푸는줄 알았다.
현재 위치를 청소한 이후, 현재 방향을 기준으로 왼쪽으로 돌면서 청소할 구역이 있다면 들어가서 해당 방향의 왼쪽방향부터 탐색을 진행한다.
여기서 주의 해야할 점은 뒤로 갈 때 인데, 네 방향 모두 청소가 다 되어있다면 그방향 그대로 후진하고 후진 방향으로 이동 한 후에도 
전부 청소되어 있다면 또 그대로 후진하는 것이다.
이걸 이해를 못해서 dfs로 푸려고 했다...
2. 또한 break문을 나오게 되면 continue처럼 위로 올라가는 것이 아니라 아래 남아있는 코드를 수행하게 된다.
'''