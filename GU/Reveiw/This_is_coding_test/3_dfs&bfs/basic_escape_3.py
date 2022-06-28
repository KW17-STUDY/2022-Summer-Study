# 탈출할 수 있는 최단 거리 출력
# 탈출이 불가능하다면 -1 출력
# n*m 크기, 네 방향 중 인접한 칸으로 이동 가능
from collections import deque

row, col = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(row)
]


def in_range(x, y):
    return x >= 0 and x < row and y >= 0 and y < row


def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 1:
        return True
    return False


def bfs(x, y):
    queue = deque([(x, y)])
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 방문처리 생략
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = cur_x+dx, cur_y+dy
            if can_go(new_x, new_y):
                queue.append((new_x, new_y))
                grid[new_x][new_y] = grid[cur_x][cur_y] + 1


bfs(0, 0)
print(grid[row-1][col-1]-1)
