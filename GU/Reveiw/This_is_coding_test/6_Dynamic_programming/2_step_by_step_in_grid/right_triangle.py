# 격자에서 한칸 씩 전진하는 DP
# 직사각형 제일 아래쪽 줄에서 가장 큰 값을 가져오기

import sys

NEG_INF = -sys.maxsize

n = 4
grid = [
    [4],
    [6, 2],
    [3, 7, 9],
    [3, 4, 9, 9]
]
dp = [[0 for _ in range(n)] for _ in range(n)]


def initialize():
    dp[0][0] = 4
    for i in range(1, n):
        dp[i][0] = grid[i][0] + dp[i-1][0]
        dp[i][i] = grid[i][i] + dp[i-1][i-1]


initialize()
for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1] + grid[i][j], dp[i-1][j]+grid[i][j])
print(dp)
print(max(dp[n-1]))

'''
#Remind
1. NEG_INF = -sys.maxsize

'''
