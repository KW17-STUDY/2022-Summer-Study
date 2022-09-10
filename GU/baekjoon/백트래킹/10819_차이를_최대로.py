#40

from itertools import permutations
n = int(input())
nums = list(map(int,input().split()))
answer = 0
def operate(nums):
    sum = 0
    for i in range(1, len(nums)):
        sum += abs(nums[i]-nums[i-1])
    return sum

for i in permutations(nums, n):
    result = operate(i)
    answer = max(result, answer)
print(answer)
