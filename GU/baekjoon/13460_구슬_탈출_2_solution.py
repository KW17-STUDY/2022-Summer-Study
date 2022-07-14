import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
# 방문을 했는지 하지 않았는지 check 하기
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()


def init():
    _rx, _ry, _bx, _by = [0]*4
    for i in range(n):
        for j in range(m):
            # 빨간 구슬 입력 받기
            if grid[i][j] == 'R':
                _rx, _ry = i, j
            elif grid[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True


def move(_x, _y, _dx, _dy, _c):
    # 다음에 벽이나 구멍이 나온다면 그 이전 까지 이동 시키기
    while grid[_x+_dx][_y+_dy] != '#' and grid[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c


def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 9:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if grid[nbx][nby] == 'O':
                continue
            if grid[nrx][nry] == 'O':
                print(d+1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)


init()
bfs()
# reference: https://rebas.kr/724
'''
# Remind
1. while grid[_x+_dx][_y+_dy]를 사용해서 다음에 벽이 있는지 없는지, hole이 있는지 없는지 확인한 후 있다면
벽이나 hole 이전 칸으로 옮겨놓는다.
나는 grid[_x][_y]을 사용해서 나중에 dx와 dy를 빼줬는데 위의 방법이 더 간단한 것 같다.
2. 4차원 배열을 사용해서 방문했던 칸인지 아닌지 아닌지 확인한다.
3. bfs로 최단거리를 풀 때, grid에 거리를 적어야한다는 생각이 드는데 이렇게 안하고 queue에 cost를 넣어서 풀면 된다.
안적고 queue를 통해 해결하는게 더 깔끔한 것 같다.
'''
