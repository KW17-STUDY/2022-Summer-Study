#4:00~4:07

import sys

INF = sys.maxsize
n = int(input())
dp = [0 for _ in range(n+1) ]
time, cost = [], []

for _ in range(n):
    t, c = map(int,input().split())
    time.append(t)
    cost.append(c)

for i in range(1, n+1):
    for j in range(i):
        if j+time[j] <= i:
            dp[i] = max(dp[i], dp[j] + cost[j])

print(dp[-1])