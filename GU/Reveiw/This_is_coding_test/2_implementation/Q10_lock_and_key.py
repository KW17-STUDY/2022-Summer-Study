from copy import deepcopy

key_num = 4
lock_num = 3

key = [
    list(map(int, input().split()))
    for _ in range(key_num)
]
lock = [
    list(map(int, input().split()))
    for _ in range(lock_num)
]


def rotation():
    global key
    # 행 갯수
    n = len(key)
    # 열 개수
    m = len(key[0])
    result = [
        [0 for _ in range(n)]
        for _ in range(m)
    ]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    key = deepcopy(result)


def in_range(row, col, i, j):
    return row + i < lock_num and col + j < lock_num and row + i >= 0 and col + j >= 0


def sum_and_rotation(row, col):
    temp = deepcopy(lock)

    for _ in range(4):
        rotation_flag = False
        rotation()
        print('------key-----')
        print(*key)
        print('------lock----')
        print(*lock)
        for i in range(key_num):
            for j in range(key_num):
                if in_range(row, col, i, j):
                    temp[row+i][col+j] = key[i][j] + lock[row+i][col+j]

        print('-------temp---------')
        print(*temp)
        for i in range(lock_num):
            for j in range(lock_num):
                if temp[i][j] != 1:
                    rotation_flag = True
        print('rotation:', rotation_flag)
        if rotation_flag == False:
            return True
    return False


# lock에서의 위치
success = False
for row in range(-lock_num, lock_num):
    for col in range(-lock_num, lock_num):
        # 더한 결과 계산 후 2나 0이 있는지 확인
        if sum_and_rotation(row, col):
            print('Success')
            success = True

if success == True:
    print('True')
else:
    print('False')

# My answer in programmers


def solution(key, lock):
    answer = False
    lock_num = len(lock)

    # 자물 쇠를 볼 위치를 정하기 위해 row, col 설정
    # -lock_num ~ lock_num 까지 해준 이유: 열쇠가 자물쇠에 걸칠 수 있기 때문
    for row in range(-lock_num, lock_num):
        for col in range(-lock_num, lock_num):
            if sum_and_rotation(key, lock, row, col):
                answer = True
    return answer


def rotation(key):
    # 행 갯수
    n = len(key)
    # 열 개수
    m = len(key[0])
    result = [
        [0 for _ in range(n)]
        for _ in range(m)
    ]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    return result


def in_range(row, col, i, j, lock_num):
    return row + i < lock_num and col + j < lock_num and row + i >= 0 and col + j >= 0


def sum_and_rotation(key, lock, row, col):
    temp = deepcopy(lock)
    key_num = len(key)
    lock_num = len(lock)
    for _ in range(4):
        rotation_flag = False
        key = rotation(key)
        # print('------key-----')
        # print(*key)
        # print('------lock----')
        # print(*lock)
        for i in range(key_num):
            for j in range(key_num):
                if in_range(row, col, i, j, lock_num):
                    temp[row+i][col+j] = key[i][j] + lock[row+i][col+j]

        # print('-------temp---------')
        # print(*temp)
        for i in range(lock_num):
            for j in range(lock_num):
                if temp[i][j] != 1:
                    rotation_flag = True
        #print('rotation:', rotation_flag)
        if rotation_flag == False:
            return True
    return False
