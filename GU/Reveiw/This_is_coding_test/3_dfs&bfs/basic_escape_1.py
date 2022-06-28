# 두 방향 탈출 가능 여부 판별
# n*m 크기, 아래와 오른쪽 2방향 중 인접한 칸으로 이동 가능
row, col = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(row)
]


def in_range(x, y):
    return x >= 0 and x < row and y >= 0 and y < col


def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 1:
        return True
    return False


dxs, dys = [1, 0], [0, 1]


def dfs(x, y):
    grid[x][y] = -1
    for dx, dy in zip(dxs, dys):
        cur_x, cur_y = x + dx, y + dy
        if can_go(cur_x, cur_y):
            dfs(cur_x, cur_y)


dfs(0, 0)
if grid[row-1][col-1] == -1:
    print(1)
else:
    print(0)

'''
# Remind
1. 기존의 simulation 문제에서는 한 step씩 확실하게 해결하고 나아가는 문제였지만,
해당 문제에서 뱀을 만나면 돌아가서 다시 계속해서 수행을 해야한다.
이에 bfs or dfs를 사용한다.
'''
