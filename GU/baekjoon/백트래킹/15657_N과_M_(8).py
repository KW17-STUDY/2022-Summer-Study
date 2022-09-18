from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int,input().split()))
nums = sorted(nums)
for combs in combinations_with_replacement(nums, m):
    for comb in combs:
        print(comb, end= ' ')
    print()