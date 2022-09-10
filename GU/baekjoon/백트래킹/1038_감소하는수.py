#52
n = int(input())
cnt = 0
answer = []
have_to_select = 0
cnt = 0

def dfs(depth, prev, extracted):
    global answer, cnt
    if depth == have_to_select:
        cnt += 1
        if cnt-1 == n:
            answer = extracted[:]
        return
    for i in range(10):
        if i < prev:
            extracted.append(i)
            dfs(depth+1, i, extracted)
            extracted.pop()

for i in range(1, 11):
    have_to_select = i
    dfs(0, 10, [])
if len(answer) == 0:
    print(-1)
else:
    print(''.join(map(str,answer)))

'''
# Remind
1. combinations로 하면 [0,1,2,3,4,5,6,7,8,9] 에서 차례대로 뽑기
때문에 [3,1]과 같은 것들을 뽑지 못함! [1,3]이라고 나오기 때문에..
그래서 dfs로 풀어준다.

2. visited를 사용하지 않아도 됨!
왜냐하면 어차피 prev보다 작은 i들만 사용하기 때문에 이전에 방문했는지
하지 않았는지는 중요하지 않음..
'''