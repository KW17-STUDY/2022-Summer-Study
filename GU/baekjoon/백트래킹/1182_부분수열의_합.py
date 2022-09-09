#30분
from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
visited = [False for _ in range(n)]

def dfs(depth, start, sum):
    global answer
    if depth!=0 and sum == s:
        answer += 1
    if depth == n:
        return
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1,sum+nums[i])
            visited[i] = False



dfs(0, 0, 0)

print(answer)


'''
*** combination 사용 버전 ***

for i in range(1, len(nums)+1):
    for j in combinations(nums, i):
        if sum(j) == s:
            answer+=1

'''
'''
1. 부분 수열이라해서 연속된 수열을 말하는 줄 알았다...
연속된 부분 수열이 아니므로 dfs나 combinations을 통해 
숫자를 골라 풀어주기.
'''