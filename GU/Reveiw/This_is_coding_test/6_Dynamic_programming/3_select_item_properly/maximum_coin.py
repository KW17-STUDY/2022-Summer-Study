import sys

goal_coin = int(input())
coins = [2, 3, 5]
NEG_INF = -sys.maxsize
dp = [NEG_INF for _ in range(goal_coin + 1)]


def initialize():
    dp[0] = 0


initialize()
for i in range(1, goal_coin+1):
    for coin in coins:
        if i >= coin:
            if dp[i-coin] != NEG_INF:
                dp[i] = max(dp[i], dp[i-coin] + 1)

print(dp)

'''
#Remind
1. dp[0]를 0로 만들고 이를 이용해 dp[2], dp[3]을 초기화
dp[5]의 경우는 초기화 해도 값이 그 값이 작아 값이 다른걸로 갱신됨.
2. NEG_INF = -sys.maxsize를 통해 만들어지지 않는 값으로 구분
'''
