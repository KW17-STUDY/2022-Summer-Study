#49~12
n = int(input())
nums = list(map(int,input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(0, i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
'''
from itertools import combinations
n = int(input())
nums = list(map(int, input().split()))
answer = 1

def check(comb):
    for i in range(1,len(comb)):
        if comb[i] < comb[i-1]:
            return False
    else:
        return True

for i in range(2, n):
    for comb in combinations(nums, i):
        if check(comb):
            answer = i
            break
    else:
        print(answer)
        break
'''