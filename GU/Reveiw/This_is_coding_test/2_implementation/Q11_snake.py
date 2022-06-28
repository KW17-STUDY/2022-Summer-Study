from collections import deque

side = int(input())
apple_num = int(input())
apple_locations = []
direction_order = []
direction = 0
head = [0, 0]
for _ in range(apple_num):
    row, col = map(int, input().split())
    apple_locations.append((row-1, col-1))

direction_coversion_num = int(input())
for _ in range(direction_coversion_num):
    time, dir = input().split()
    time = int(time)
    direction_order.append((time, dir))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동 남 서 북

snake_grid = [
    [0 for _ in range(side)]
    for _ in range(side)
]
apple_grid = [
    [0 for _ in range(side)]
    for _ in range(side)
]

# 뱀은 0,0 부터 시작
snake_grid[0][0] = 1

# 사과 setting
for x, y in apple_locations:
    apple_grid[x][y] = 1


def can_go(new_head):
    if in_range(new_head) and snake_grid[new_head[0]][new_head[1]] != 1:
        # [new_head[0], new_head[1]] not in snake_history:
        return True
    return False


def in_range(new_head):
    return new_head[0] < side and new_head[0] >= 0 and new_head[1] < side and new_head[1] >= 0


snake_history = deque([[head[0], head[1]]])
t = 0
new_head = [0, 0]
cur_direction = directions[direction]

while True:
    new_head[0], new_head[1] = head[0] + \
        cur_direction[0], head[1]+cur_direction[1]
    # 시간 증가
    t += 1
    # 부딪혔는지 아닌지 검사
    if not can_go(new_head):
        break

    # 사과가 있는지 검사
    # apple이 없을 경우
    if apple_grid[new_head[0]][new_head[1]] == 0:
        x, y = snake_history.pop()
        snake_grid[x][y] = 0

    # snkae 이동
    # head = new_head라고 하면 안됨.
    # ailiasing 발생
    head[0], head[1] = new_head[0], new_head[1]
    snake_grid[head[0]][head[1]] = 1
    snake_history.appendleft([head[0], head[1]])

    # direction을 변경해야하면 고개를 틀기
    for event_time, cur_direct in direction_order:
        if event_time == t:
            if cur_direct == 'L':
                direction -= 1
            else:
                direction += 1
            direction %= 4
            cur_direction = directions[direction]

print(t)

'''
# Remind
1. queue나 deque에 넣을 때, 객체를 넣지 않고 value로 넣는다.
2. direction = (direction - 1)%4 => 4가지 방향이 존재할 때 사용
'''
