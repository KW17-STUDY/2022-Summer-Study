# 최대 증가 부분 수열
# https://www.acmicpc.net/problem/11053
import sys

NEG_INF = -sys.maxsize

n = int(input())
temp_arr = list(map(int, input().split()))
arr = [0] + temp_arr
dp = [NEG_INF for _ in range(n+1)]


def initialize():
    dp[0] = 0


initialize()
for i in range(1, n+1):
    for j in range(i):
        # 아래 if문은 안넣어줘도 된다.
        # NEG_INF가 나올 수 없게 dp의 0번째 index를 0으로 만들어서 무조건 1이 초반에 들어갈 수 밖에 없기 때문
        if arr[j] != NEG_INF:
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
'''
1.dp를 n+1크기로 해주어 0번째 index로 첫번째 index를 자연스럽게 초기화할 수 있도록 한다.
또한 0보다 큰 수를 갖고있는 index의 dp값을 자연스럽게 1로 만들 수 있도록 한다(무조건 1 이상의 값이 들어오기 때문에.).
'''
