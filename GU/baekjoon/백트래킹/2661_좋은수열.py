#1시간
n = int(input())

def check(extracted, length):
    check_len = length//2
    for i in range(2, check_len+1):# 차이
        for j in range(0, length):#0부터 끝까지
            if j+i > length or j+i+i > length:
                break
            cur = extracted[j:j+i]
            next = extracted[j+i:j+i+i]
            if cur==next:#두개가 같다면
                return False
    return True


def recursive(depth, prev, extracted):
    global n
    if depth == n:
        print(''.join(extracted))
        exit()
        
    for i in ['1','2','3']:
        if i != prev:
            extracted.append(i)
            if check(extracted, len(extracted)):
                recursive(depth+1, i, extracted)
            extracted.pop()


recursive(1, '1',['1'])
'''
1. 기존에 n까지 자릿수를 다 만들고 check()해서 조건에 맞지 않으면 재귀를 통해 계속 탐색해나가는 방식으로 풀었다.
그 check함수를 마지막에 해주는게아니라 매번 새로운 숫자를 넣어주고 검사시켜서 재귀안으로 많이 들어가는 것을 방지해서 풀었다.
이것이 가지치기!!
back tracking은 for문 안에 들어가는 if문을 잘 설정하는 것이 중요한 것 같다.
왜냐하면 가지치기는 필요없는 재귀 안으로 들어가게하지 않는 것이니까!

-기존 recursive 소스코드

def recursive(depth, prev, extracted):
    global n
    if depth == n:
        if check(extracted, depth): => n까지 다 만들면 check했었음. 이렇게 하면 backtracking이 아님.
            print(''.join(extracted))
            exit()
        return
    for i in ['1','2','3']:
        if i != prev: => for문의 if문 에서 처리해야 backtracking이다.
            extracted.append(i)
            recursive(depth+1, i, extracted)
            extracted.pop()
'''