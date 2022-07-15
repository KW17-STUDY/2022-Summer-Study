jump = [2, 3, 0, 1, 4]
n = 5
dp = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        # 현재 위치가 전의 위치+전의 위치에서 뛸수 있는 크기랑 같거나 작아야함.
        if i <= j + jump[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(dp)
