row, virus_num = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(row)
]
s, x, y = tuple(map(int, input().split()))


def in_range(x, y):
    return x >= 0 and x < row and y >= 0 and y < row


def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 0:
        return True
    return False


def propagation(x, y, virus):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            # 이번 step에 update해준것은 -로 표현
            grid[new_x][new_y] = -virus


    # s초 동안 실행
for _ in range(s):
    # for b in range(row):
    #     for c in range(row):
    #         print(grid[b][c], end=' ')
    #     print()
    # print()
    # 1번부터 k까지 바이러스 전파
    for virus in range(1, virus_num+1):
        # 해당 virus를 2차원 평면에서 찾기
        for i in range(row):
            for j in range(row):
                if grid[i][j] == virus:
                    # 전파
                    propagation(i, j, virus)

    # -로 표현된 현재 step에 update된 값들을 모두 양수로 변형
    for i in range(row):
        for j in range(row):
            if grid[i][j] < 0:
                grid[i][j] = -grid[i][j]


print(grid[x-1][y-1])

'''
1. simulation 문제이므로(한 step마다 확정지어짐) 기존의 전역변수에 저장되어 있었던 것을 따로 저장해 둘 필요가 없으므로
그냥 전역변수를 수정하면됨.
Q16_laboratory처럼 초기 상태를 저장해줄 필요가 없다->Q16은 기존의 wall의 위치만을 기억해둬야 했기 때문에 deepcopy를 사용해서
전역변수인 grid의 초기값을 유지하고 temp_grid사용.
'''
