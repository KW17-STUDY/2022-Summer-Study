# 부품 찾기
# 전체 부품: 1~1,000,000
# 찾으려는 부품: 1~100,000
# 100만의 데이터를 다루려면 최소 nlogn으로 풀어야함 -> sort를 생각할 수 있다.
# sort를 한 뒤에 이진 탐색 수행.
import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] < target:
        start = mid+1
        return binary_search(array, target, start, end)
    elif array[mid] > target:
        end = mid - 1
        return binary_search(array, target, start, end)
    else:
        return array[mid]


input = sys.stdin.readline
total_num = int(input())
total = list(map(int, input().split()))
search_comp_num = int(input())
comp_num = list(map(int, input().split()))

total.sort()
for i in comp_num:
    result = binary_search(total, i, 0, len(total)-1)
    if not result:
        print('no', end=' ')
    else:
        print('yes', end=' ')
