n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
visited = [False for _ in range(n)]
def dfs(depth, start, extracted):
    if depth == m:
        print(' '.join(map(str,extracted)))
        return
    for i in range(start, n):
        if not visited[i]:
            extracted.append(nums[i])
            dfs(depth+1, i+1, extracted)
            extracted.pop()

dfs(0, 0, [])
