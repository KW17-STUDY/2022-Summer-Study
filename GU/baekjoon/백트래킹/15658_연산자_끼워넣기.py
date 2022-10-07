#11~18
#58
import sys

n = int(input())
nums = list(map(int, input().split()))
operations = list(map(int,input().split()))
MIN, MAX = sys.maxsize, -sys.maxsize
len = len(nums)

def dfs(depth, value):
    global MIN, MAX, operations
    if depth == len:
        MIN = min(MIN, value)
        MAX = max(MAX, value)
        return
    for i in range(4):
        if operations[i] > 0:
            operations[i] -= 1
            if i == 0:
                dfs(depth+1,value+nums[depth])
            elif i == 1:
                dfs(depth+1,value-nums[depth])
            elif i == 2:
                dfs(depth+1,value*nums[depth])
            else:
                if value < 0:
                    dfs(depth+1,-((-value)//nums[depth]))
                else:
                    dfs(depth+1,value//nums[depth])
            operations[i] += 1


dfs(1, nums[0])
print(MAX)
print(MIN)