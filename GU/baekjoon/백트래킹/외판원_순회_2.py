import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [False for _ in range(n)]
MIN = 1e9
start_point = None

def dfs(depth, now, cost):
    global start_point, visited, MIN
    # 총 도시가 n일 경우, depth가 n-1일 때 전체 도시를 방문 했던 것이다.
    # depth 0:   시작점만 포함
    # depth n-1: 전체 도시 순회 
    if depth == n-1:
        # 마지막에 방문했던 도시에서 시작점으로 가는 루트 더해주기
        # 시작점으로 가는 cost가 0인경우 없으므로 return
        if grid[now][start_point] == 0:
            return
        temp = grid[now][start_point] + cost
        MIN = min(temp, MIN)
        # return 잊지말기
        return

    for i in range(n):
        if not visited[i] and grid[now][i] != 0:
            visited[i] = True
            dfs(depth+1, i, cost+grid[now][i])
            visited[i] = False


for i in range(n):
    start_point = i
    visited[i] = True
    # 시작점 i로 설정
    dfs(0, i, 0)
    visited[i] = False

print(MIN)