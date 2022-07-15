# subproblem을 그대로 합치면 되는 DP

n = int(input())
dp = [0 for _ in range(n+1)]


def initialize():
    dp[1] = 1
    dp[2] = 1


initialize()
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp)

'''
# Remind
1. Dp의 전형적인 틀
① dp table 결정
② dp table 초기화
③ 점화식 결정
2. 항상 마지막에 무엇을 하고 반복되는지 살펴보기

'''
