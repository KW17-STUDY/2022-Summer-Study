n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
visited = [False for _ in range(n)]

def dfs(depth, extracted):
    if depth == m:
        print(' '.join(map(str,extracted)))
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != nums[i]:
            extracted.append(nums[i])
            visited[i] = True
            prev = nums[i]
            dfs(depth+1, extracted)
            visited[i] = False
            extracted.pop()

#dfs(0, [])


from itertools import combinations_with_replacement
from itertools import combinations

for i in combinations_with_replacement(nums, m):
    print(' '.join(map(str,i)))
print('--------------------------')
for i in combinations([1,1,1,1], m):
    print(' '.join(map(str,i)))
print('--------------------------')
for i in combinations_with_replacement([1,2,3,4], m):
    print(' '.join(map(str,i)))
