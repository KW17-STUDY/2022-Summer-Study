from itertools import permutations


n = int(input())
for i in permutations([i for i in range(1,n+1)], n):
    print(' '.join(map(str,i)))

'''
visited = [False for _ in range(n+1)]

def dfs(depth, extracted):
    if depth == n:
        print(' '.join(map(str, extracted)))
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            extracted.append(i)
            dfs(depth+1, extracted)
            visited[i] = False
            extracted.pop()
dfs(0, [])
'''