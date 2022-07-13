# 빨간색 공, 파란색 공
# 동시에 움직임
# 빨간색 구멍에 빠지면 성공,파란색 빠지거나 동시에 빠지면 실패
# 최소 몇 번만에 뺄 수 있는지
from collections import deque

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
print(n, m)
print(grid)


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
        elif grid[i][j] == 'R':
            r_queue.append((i, j))
            R_grid[i][j] = 0
        else:
            B_grid[i][j] = '.'
            R_grid[i][j] = '.'
Success = False
OVER = False


def bfs():
    global OVER
    while r_queue and b_queue:
        print('r_queue:', r_queue)
        print('b_queue:', b_queue)
        if OVER == True:
            break
        r_x, r_y = r_queue.popleft()
        b_x, b_y = b_queue.popleft()
        dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
        for dx, dy in zip(dxs, dys):
            print(dx, dy)
            new_r_x, new_r_y = r_x + dx, r_y + dy
            new_b_x, new_b_y = b_x + dx, b_y + dy
            # 둘 다 해당 방향으로 갈 수 있다면
            # '.'끝까지 전진
            # hole에 빠졌는지 아닌지 검사
            B_flag = False
            R_flag = False

            # 몇번 걸렸는지 횟수 적기
            r_num = R_grid[r_x][r_y] + 1
            b_num = B_grid[b_x][b_y] + 1
            print('r_num:', r_num)
            print('b_num:', b_num)
            if r_num >= 10 or b_num >= 10:
                OVER = True
                break
            R_grid[new_r_x][new_r_y] = r_num
            B_grid[new_b_x][new_b_y] = b_num

            # 돌아와야 하므로 이전의 좌표를 기억하기
            pre_b_x = new_b_x
            pre_b_y = new_b_y
            pre_r_x = new_r_x
            pre_r_y = new_r_y

            # hole까지 몇번만에 갔는지 세기
            r_count = 0
            b_count = 0
            while B_grid[new_b_x][new_b_y] != '#':
                print(dx, dy)
                pre_b_x = new_b_x
                pre_b_y = new_b_y
                if B_grid[new_b_x][new_b_y] == '0':
                    print('in the hole')
                    print('new_b_x: ', new_b_x, 'new_b_y: ', new_b_y)
                    B_flag = True
                    break
                b_count += 1
                new_b_x, new_b_y = new_b_x + dx, new_b_y + dy
                print('new_b_x: ', new_b_x, 'new_b_y: ', new_b_y)

            while R_grid[new_r_x][new_r_y] != '#':
                print('new_r_x: ', new_r_x, 'new_r_y: ', new_r_y)
                pre_r_x = new_r_x
                pre_r_y = new_r_y
                if R_grid[new_r_x][new_r_y] == '0':
                    print('in the hole')
                    print('new_r_x: ', new_r_x, 'new_r_y: ', new_r_y)
                    R_flag = True
                    break
                r_count += 1
                new_r_x, new_r_y = new_r_y + dx, new_r_y + dy
            # 성공
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
                r_queue.append((pre_r_x, pre_r_y))
                b_queue.append((pre_b_x, pre_b_y))


bfs()
if OVER == True:
    print('타임 아웃')

print(Success)
