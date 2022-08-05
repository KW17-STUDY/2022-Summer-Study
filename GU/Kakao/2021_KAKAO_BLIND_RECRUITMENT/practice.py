from bisect import bisect_left, bisect_right

nums = [0,1,2,3,4,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))