# My answer
n = input()
length = len(n)

# 2부분으로 나누기
front = n[0:int(length/2)]
end = n[int(length/2):]

# list로 바꾼후 각각의 element를 map을 이용해서 int로 변환하기
front = map(int, list(front))
end = map(int, list(end))

# Sum하기
sum_front = sum(front)
sum_end = sum(end)

if sum_front == sum_end:
    print('LUCKY')
else:
    print('READY')

# Another answer
n = input()
length = len(n)
summary = 0

# index로 접근하면서 int로 바꿔 하나씩 더 해주기
for i in range(length//2):
    summary += int(n[i])

# index로 접근하면서 int로 바꿔 하나씩 빼주기
for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')

'''
# remind
1. 문자열도 index로 접근 가능
2. 문자열도 for ~ in으로 받기 가능
3. length/2->float로 나오지만 length//2는 int로 나온다.
4. My answer의 경우, 앞과 뒤를 미리 나누어 따로따로 계산했지만
Anotehr answer의 경우 미리 나누지 않고 index로 접근해서 계산하였다.

'''
