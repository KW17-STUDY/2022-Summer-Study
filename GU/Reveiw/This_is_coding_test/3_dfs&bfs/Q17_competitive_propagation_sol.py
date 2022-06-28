# bfs 사용
from collections import deque

n, k = map(int, input().split())
grid = []

# 초기 바이러스에 대한 정보를 담는 data
data = []


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 0:
        return True
    return False


for i in range(n):
    grid.append(list(map(int, input().split())))
    for j in range(n):
        if grid[i][j] != 0:
            data.append((grid[i][j], 0, i, j))

#default: 오름차순
data.sort()
queue = deque(data)
# 방문처리 생략 -> 이미 초기화로 되어있음

target_s, target_x, target_y = map(int, input().split())
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

while queue:
    virus, s, x, y = queue.popleft()
    if target_s == s:
        break
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            queue.append((virus, s+1, new_x, new_y))
            grid[new_x][new_y] = virus

print(grid[target_x-1][target_y-1])

'''
1. 하나의 대상 주위에 있는 것들을 탐색한다면 bfs로 어떻게 풀지 생각하기
   가장 낮은 바이러스가 먼저 1step만큼 전파되어야 하니까 sort를 사용해서
   오름차순으로 정렬한 뒤에 queue안에 넣기.
2. data.sort()->오름차순 정렬, data.sort(reverse = True)->내림차순 정렬
   data.sort(key=lambda x: (x[1], x[0]))이렇게 사용가능
'''
