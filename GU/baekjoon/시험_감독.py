#40
n = int(input())
people = list(map(int, input().split()))
b, c = map(int,input().split())
answer = 0
for i in range(len(people)):
    answer += 1
    people[i] -= b
    if people[i] < 0:
        people[i] = 0

for i in range(len(people)):
    if people[i] == 0:
        continue
    value, remain = divmod(people[i], c)
    answer += value+1 if remain !=0 else value

print(answer)


