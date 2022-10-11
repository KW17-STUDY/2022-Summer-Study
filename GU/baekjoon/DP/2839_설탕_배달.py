#44
import sys

target = int(input())
INF = sys.maxsize
dp = [INF for _ in range(target+1)]
dp[0] = 0
kilos = [3, 5]

for kilo in kilos:
    for i in range(1, target+1):
        if i-kilo >= 0 and dp[i-kilo] != INF:
            dp[i] = min(dp[i], dp[i-kilo]+1)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
print(dp)
        
