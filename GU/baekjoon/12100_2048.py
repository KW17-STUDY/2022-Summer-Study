from copy import deepcopy
import sys

n = int(input())
grid = [list(map(int, input().split()))for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상, 하, 좌, 우
cases = []
case_list = []
maximum_value = -sys.maxsize
origin_grid = deepcopy(grid)


def makeCases(depth):
    global case_list, cases
    if depth == 5:
        # cases.append(case_lit)라고 하면 error가 난다.
        # 파이썬은 포인터로 이루어져 있어서 case_list자체를 넣으면
        # case_list가 가리키고 있는 값들이 항상 바뀌기 때문에
        # cases안에 존재하는 값들이 case_list가 바뀔 때마다 바뀌어버린다.
        cases.append(case_list[:])
        return
    for i in range(4):
        case_list.append(i)
        makeCases(depth+1)
        case_list.pop()


def compareAndSum(direction):
    if direction == 0:  # 위로 이동
        for i in range(n):
            prior_value = grid[0][i] if grid[0][i] != 0 else None
            prior_index = 0 if grid[0][i] != 0 else None
            for j in range(1, n):
                if grid[j][i] == 0:
                    continue
                if grid[j][i] == prior_value:
                    # 값이 같으므로 2배로 만들어 준 이후, prior_Value값도 수정
                    # 더해주었으므로 원래 자리 것을 지워주기
                    grid[prior_index][i] = prior_value * 2
                    prior_value, prior_index = None, None
                    grid[j][i] = 0
                else:
                    # 값이 다르므로 prior_value와 index 고치기
                    prior_value = grid[j][i]
                    prior_index = j
    elif direction == 1:  # 아래쪽으로 이동
        for i in range(n):
            prior_value = grid[n-1][i] if grid[n-1][i] != 0 else None
            prior_index = n-1 if grid[n-1][i] != 0 else None
            for j in range(n-2, -1, -1):
                if grid[j][i] == 0:
                    continue
                if grid[j][i] == prior_value:
                    # 값이 같으므로 2배로 만들어 준 이후, prior_Value값도 수정
                    # 더해주었으므로 원래 자리 것을 지워주기
                    grid[prior_index][i] = prior_value * 2
                    prior_value, prior_index = None, None
                    grid[j][i] = 0
                else:
                    # 값이 다르므로 prior_value와 index 고치기
                    prior_value = grid[j][i]
                    prior_index = j
    elif direction == 2:  # 왼쪽으로 이동
        for i in range(n):
            prior_value = grid[i][0] if grid[i][0] != 0 else None
            prior_index = 0 if grid[i][0] != 0 else None
            for j in range(1, n):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == prior_value:
                    # 값이 같으므로 2배로 만들어 준 이후, prior_Value값도 수정
                    # 더해주었으므로 원래 자리 것을 지워주기
                    grid[i][prior_index] = prior_value * 2
                    prior_value, prior_index = None, None
                    grid[i][j] = 0
                else:
                    # 값이 다르므로 prior_value와 index 고치기
                    prior_value = grid[i][j]
                    prior_index = j
    else:  # 오른쪽으로 이동
        for i in range(n):
            prior_value = grid[i][n-1] if grid[i][n-1] != 0 else None
            prior_index = n-1 if grid[i][n-1] != 0 else None
            for j in range(n-2, -1, -1):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == prior_value:
                    # 값이 같으므로 2배로 만들어 준 이후, prior_Value값도 수정
                    # 더해주었으므로 원래 자리 것을 지워주기
                    grid[i][prior_index] = prior_value * 2
                    prior_value, prior_index = None, None
                    grid[i][j] = 0
                else:
                    # 값이 다르므로 prior_value와 index 고치기
                    prior_value = grid[i][j]
                    prior_index = j


def move(direction):
    global grid
    if direction == 0:  # 상
        temp = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):  # 하나의 열
            point = 0
            for j in range(n):
                if grid[j][i] != 0:
                    temp[point][i] = grid[j][i]
                    point += 1
        grid = deepcopy(temp)
    elif direction == 1:  # 하
        temp = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):  # 하나의 열
            point = n-1
            for j in range(n-1, -1, -1):
                if grid[j][i] != 0:
                    temp[point][i] = grid[j][i]
                    point -= 1
        grid = deepcopy(temp)
    elif direction == 2:  # 좌
        for i in range(n):  # 4개의 row
            temp = [0 for _ in range(n)]
            point = 0
            for j in range(n):
                if grid[i][j] != 0:
                    temp[point] = grid[i][j]
                    point += 1
            grid[i] = temp[:]
    else:  # 우
        for i in range(n):  # 4개의 row
            temp = [0 for _ in range(n)]
            point = n-1
            for j in range(n-1, -1, -1):
                if grid[i][j] != 0:
                    temp[point] = grid[i][j]
                    point -= 1
            grid[i] = temp[:]


def findMaxValue():
    max_value = -sys.maxsize
    for i in range(n):
        for j in range(n):
            if max_value < grid[i][j]:
                max_value = grid[i][j]
    return max_value


# 앞쪽부터 두 개가 같은지 확인
# 같다면 앞에 것을 기준으로 더해주기
makeCases(0)
for directions in cases:
    grid = deepcopy(origin_grid)
    for direction in directions:
        compareAndSum(direction)
        move(direction)
    value = findMaxValue()
    if maximum_value < value:
        maximum_value = value
print(maximum_value)
