# 진행하다 끊기고 진행하다가 끊기는 Dp
# 연속 부분 합의 최대 값 구하기
# https://www.acmicpc.net/problem/1912
import sys

NEG_INF = -sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
dp = [NEG_INF for _ in range(n)]


def initialize():
    dp[0] = arr[0]


initialize()
for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))
'''
1. dp[i]의 의미: i번쨰 index를 꼭 포함하는 최대합
2. dp[i]가 i번째 index를 꼭 포함하는 최대합이므로 max를 사용해서 제일 큰 수를 찾으면
그 수가 가장큰 연속 부분의 합이 된다.
3. 이전에도 생각해보면 해당 index를 꼭 포함할 때 였는데, 지금의 경우도 i번째까지 꼭 포함하는 경우를 의미함.
4. 상태로 dp table를 만드는 경우가 있음.
i번째 까지 시행했고 j번 파란색 카드를 뽑고 i-j번 빨간색 카드를 뽑은 경우,
dp[i][j]에 표기
'''
