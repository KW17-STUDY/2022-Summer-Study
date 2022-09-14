# 20
n, m = map(int, input().split())
nums = map(int,input().split())
nums = sorted(nums)
visited = [False for _ in range(n)]
def dfs(depth, extracted):
    if depth == m:
        print(' '.join(map(str,extracted)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            extracted.append(nums[i])
            dfs(depth + 1, extracted)
            visited[i] = False
            extracted.pop()
dfs(0, [])

'''
# Remind
nums = map(int,input().split())같이 int로 변형해주고 sort해주어야 한다.
int로 변환하고 input().split()만 사용했더니 에러가 남..
조심하자..!
'''

'''
from itertools import permutations

n, m = map(int, input().split())
nums = map(int,input().split())
nums = sorted(nums)

def printFormat(comb):
    for i in comb:
        print(i, end= ' ')
    print()

for i in permutations(nums, m):
    printFormat(i)
'''