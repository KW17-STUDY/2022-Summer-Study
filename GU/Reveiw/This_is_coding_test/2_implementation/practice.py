from collections import deque
s = [1, 2, 3, 4, 5, 6, 7]
length = len(s)
for i in range(0, length, 3):
    print(s[i])
print(s[4:100])

grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(grid[-2][-2])

print(-1 % 3)


deq = deque()
deq.appendleft(1)
print(deq)
deq.appendleft(2)
print(deq)
deq.appendleft(3)
print(deq)
deq.appendleft(4)
print(deq)
deq.pop()
print(deq)
deq.pop()
print(deq)


deq = deque()
deq.appendleft([1, 2])
print(deq)
deq.appendleft([2, 3])
print(deq)
deq.appendleft([3, 4])
print(deq)
deq.appendleft([4, 5])
print(deq)
deq.pop()
print(deq)
deq.pop()
print(deq)
