#26
n = int(input())
dp = [0 for _ in range(n+1)]
if n < 4:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[-1]%10007)

