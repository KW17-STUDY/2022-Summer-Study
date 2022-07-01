array = list(map(int, input().split()))
target = int(input())
length = len(array)


def binary_search(start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    print('start:', start, end=' ')
    print('end:', end, end=' ')
    print('mid:', mid)
    if array[mid] > target:
        end = mid - 1
        return binary_search(start, end)
    elif array[mid] < target:
        start = mid + 1
        return binary_search(start, end)
    else:
        return array[mid]


result = binary_search(0, length-1)
print(result)
if result:
    print(str(result)+'(이)가 있습니다.')
else:
    print("값이 없습니다.")

'''
1. sys.stdin.readline().rstrip(): 마지막 개행 제거
'''
