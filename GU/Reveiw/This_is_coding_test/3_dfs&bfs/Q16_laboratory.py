from itertools import product
from itertools import combinations
from copy import deepcopy

row, col = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(row)
]
coordinates = product([i for i in range(row)], [i for i in range(col)])
# print(list(combinations(list(coordinates), 3)))
_3_coordinates = list(combinations(list(coordinates), 3))

max_safe_area = -1
viruses = []


def in_range(x, y):
    return x >= 0 and x < row and y >= 0 and y < col


def can_go(x, y, temp_grid):
    if in_range(x, y) and temp_grid[x][y] == 0:
        return True
    return False


def dfs(x, y, temp_grid):
    temp_grid[x][y] = 2
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y, temp_grid):
            dfs(new_x, new_y, temp_grid)


def propagation_count():
    count = 0
    temp_grid = deepcopy(grid)
    for x, y in viruses:
        dfs(x, y, temp_grid)
    for i in range(row):
        for j in range(col):
            if temp_grid[i][j] == 0:
                count += 1
    # for i in range(row):
    #     for j in range(col):
    #         print(temp_grid[i][j], end=' ')
    #     print()
    # print()
    return count


def install(a, b, c):
    grid[a[0]][a[1]] = 1
    grid[b[0]][b[1]] = 1
    grid[c[0]][c[1]] = 1


def de_install(a, b, c):
    grid[a[0]][a[1]] = 0
    grid[b[0]][b[1]] = 0
    grid[c[0]][c[1]] = 0


# 바이러스 위치 찾기
for r in range(row):
    for c in range(col):
        if grid[r][c] == 2:
            viruses.append((r, c))

# 벽을 설치할 3곳 선정 후 설치
for a, b, c in _3_coordinates:
    if not (grid[a[0]][a[1]] == 0 and grid[b[0]][b[1]] == 0 and grid[c[0]][c[1]] == 0):
        continue
    install(a, b, c)
    # for i in range(row):
    #     for j in range(col):
    #         print(grid[i][j], end=' ')
    #     print()
    # print()
    # 바이러스 전파 후 안전 지대 갯수 세기
    count = propagation_count()
    max_safe_area = max(max_safe_area, count)
    de_install(a, b, c)
print(max_safe_area)

'''
1. 전역변수인 grid를 초기상태로 보존해야하는데 grid를 수정해야하므로(wall을 설치하고, virus를 전파시켜야하므로) 2가지 방법이 존재.
(1) 나의 답처럼 deepcopy를 사용하여 temp_grid를 사용
(2) 전역변수인 grid를 수정하고 다시 고쳐놓고, 수정하고 고쳐놓고 하면서 사용.
답안을 보게되면 backtracking의 구조를 띄고 있으며 (2)의 방법을 사용!!
2. 좌표들의 조합을 만들기 위해 숫자들의 product를 만들고 이것의 combination을 구했다.
답안에서는 backtracking 구조를 사용해서 같은 위치에 꽂았던 wall의 조합((1,2,3),(2,1,3) 그대로 사용)이라도 그대로 사용한다.
'''
