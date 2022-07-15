# 빨간색 공, 파란색 공
# 동시에 움직임
# 빨간색 구멍에 빠지면 성공,파란색 빠지거나 동시에 빠지면 실패
# 최소 몇 번만에 뺄 수 있는지
from collections import deque
from distutils.log import debug

n, m = map(int, input().split())
grid = [
    list(input())
    for _ in range(n)
]
R_grid = [
    [0 for _ in range(m)] for _ in range(n)
]

B_grid = [
    [0 for _ in range(m)] for _ in range(n)
]

Success = False
OVER = False
debug_count = 0


def in_range(x, y):
    return x >= 1 and y >= 1 and x < m-1 and y < m-1

# 해당방향으로 갈 수 있는지 없는지만 검사


r_queue = deque()
b_queue = deque()


# 복사
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            R_grid[i][j] = '#'
            B_grid[i][j] = '#'
        elif grid[i][j] == 'B':
            b_queue.append((i, j))
            B_grid[i][j] = 0
            R_grid[i][j] = '.'
        elif grid[i][j] == 'R':
            r_queue.append((i, j))
            R_grid[i][j] = 0
            B_grid[i][j] = '.'
        elif grid[i][j] == 'O':
            R_grid[i][j] = 'O'
            B_grid[i][j] = 'O'
        else:
            B_grid[i][j] = '.'
            R_grid[i][j] = '.'

print('----initial R_grid----')
for i in range(n):
    for j in range(m):
        print(R_grid[i][j], end=' ')
    print()

print('----initial B_grid----')
for i in range(n):
    for j in range(m):
        print(B_grid[i][j], end=' ')
    print()


def bfs():
    global OVER
    global Success
    while r_queue and b_queue:
        print('r_queue:', r_queue)
        print('b_queue:', b_queue)
        r_x, r_y = r_queue.popleft()
        b_x, b_y = b_queue.popleft()
        print('pop 된 red:', r_x, r_y)
        print('pop된 blue:', b_x, b_y)
        dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

        for dx, dy in zip(dxs, dys):
            print('----R_grid----')
            for i in range(n):
                for j in range(m):
                    print(R_grid[i][j], end=' ')
                print()

            print('----B_grid----')
            for i in range(n):
                for j in range(m):
                    print(B_grid[i][j], end=' ')
                print()
            r_count = 1
            b_count = 1

            B_flag = False
            R_flag = False

            r_num = R_grid[r_x][r_y] + 1
            b_num = B_grid[b_x][b_y] + 1
            print('r_num:', r_num)
            print('b_num:', b_num)
            if r_num >= 10 or b_num >= 10:
                OVER = True
                return -1

            new_r_x, new_r_y = r_x + dx, r_y + dy
            new_b_x, new_b_y = b_x + dx, b_y + dy
            while True:
                print('new_r_x: ', new_r_x, 'new_r_y: ', new_r_y)
                # '#'를 만날때 까지 계속 이동
                print('R_grid[new_r_x][new_r_y] 값:', R_grid[new_r_x][new_r_y])
                if R_grid[new_r_x][new_r_y] == '#':
                    # 이전 위치 복구
                    print('벽에 막힘!')
                    new_r_x, new_r_y = new_r_x - dx, new_r_y - dy
                    break
                if R_grid[new_r_x][new_r_y] == 'O':
                    print('In the Hole!')
                    R_flag = True
                R_grid[new_r_x][new_r_y] = r_num
                new_r_x, new_r_y = new_r_x + dx, new_r_y + dy
                r_count += 1

            while True:
                print('new_b_x: ', new_b_x, 'new_b_y: ', new_b_y)
                if B_grid[new_b_x][new_b_y] == '#':
                    # 이전 위치 복구
                    print('벽에 막힘!')
                    new_b_x, new_b_y = new_b_x - dx, new_b_y - dy
                    break
                if B_grid[new_b_x][new_b_y] == 'O':
                    print('In the Hole!')
                    B_flag = True
                B_grid[new_b_x][new_b_y] = b_num
                new_b_x, new_b_y = new_b_x + dx, new_b_y + dy
                b_count += 1

            if R_flag == True and B_flag == False:
                Success = True
            # 실패
            elif R_flag == False and B_flag == True:
                Success = False
            elif R_flag == True and B_flag == True:
                # 빨간색이 먼저 들어간 경우 성공
                if r_count < b_count:
                    Success = True
                # 그렇지 않으면 싪패
                else:
                    Success = False
            else:
                r_queue.append((new_r_x, new_r_y))
                b_queue.append((new_b_x, new_b_y))

                global debug_count
                debug_count += 1
                print('----R_grid----')
                for i in range(n):
                    for j in range(m):
                        print(R_grid[i][j], end=' ')
                    print()

                print('----B_grid----')
                for i in range(n):
                    for j in range(m):
                        print(B_grid[i][j], end=' ')
                    print()
                if debug_count == 2:
                    return


bfs()
print('Success:', Success)
print('OVER:', OVER)
