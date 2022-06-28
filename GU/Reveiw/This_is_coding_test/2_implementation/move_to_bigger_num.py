n, x, y = map(int, input().split())
init_x, init_y = x, y
x, y = x-1, y-1
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def can_go(new_x, new_y):
    if not in_range(new_x, new_y) or grid[x][y] >= grid[new_x][new_y]:
        return False
    return True


dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
while True:
    print(grid[x][y], end=" ")
    prev_x, prev_y = x, y
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            x, y = new_x, new_y
            # break 안붙여줘서 error가 났었음.
            break
    # Update가 이루어지지 않았다면:
    if prev_x == x and prev_y == y:
        break

'''
# Remind
1. break 적절히 붙히기
    28번 째 줄에 break문 안붙혀줘서 error가 났었다.
    다음으로 이동할 수 있다면 더 이상 상하좌우 방향으로 되는 방향을 찾지 않아도 되므로 
    break문 사용해야 한다.
2. 더 이상 이동할 수 없을 때는 상하좌우 방향에 자신보다 큰 수가 없을 때 이다.
   이 때, 2가지 방법으로 구현 가능하다.
   (1) 위에서 사용한 방식 처럼 이전과 지금의 위치가 같은지 다른지 확인한다.
   즉, update가 일어났는지 일어나지 않았는지 확인해서 update가 일어나지 않았으면 이동할 수
   있는 칸이 없다는 의미이므로 그만한다.
   (2) 함수로 구현해서 더이상 이동할 수 없다면 False를 반환시킨다.
   해당 False를 받게 되면 더 이상 update 되지 않는다는 의미이므로 그만한다.
'''

# 2.(2)의 방법으로 구현한 simulate 코드


def simulate():
    global x, y
    print(grid[x][y], end=' ')
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            x, y = new_x, new_y
            return True
    return False


print()

x, y = init_x-1, init_y-1

while True:
    result = simulate()
    if not result:
        break
