#57
import sys
INF = sys.maxsize

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF for _ in range(3)]for _ in range(n)]

def initialize():
    global dp
    dp[0] = grid[0][:]

initialize()
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j!=k:
                dp[i][j] = min(dp[i][j], dp[i-1][k]+grid[i][j])
print(min(dp[-1]))

    