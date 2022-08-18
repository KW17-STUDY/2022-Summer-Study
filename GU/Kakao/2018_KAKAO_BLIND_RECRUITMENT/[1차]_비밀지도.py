#link: https://school.programmers.co.kr/learn/courses/30/lessons/17681
#7:59~8:28
#30분
def makeBin(num, n):
    result = []
    while num!=0:
        value, remain = divmod(num,2)
        result.append(remain)
        num = value
    while len(result)!=n:
        result.append(0)
    return result[::-1]

def solution(n, arr1, arr2):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    # arr1을 answer에 반영
    for i in range(n):
        result = makeBin(arr1[i],n)
        answer[i] = result[:]
        
    # arr2를 answer에 반영
    for i in range(n):
        result = makeBin(arr2[i],n)
        for j in range(n):
            if result[j] == 1:
                answer[i][j] = 1
    # 1을 '#'으로, 0을 ' '으로 변환
    for i in range(n):
        for j in range(n):
            answer[i][j] = '#' if answer[i][j] == 1 else ' '
    
    #list를 문자열로 변환
    for i in range(n):
        answer[i] = ''.join(answer[i])
    return answer

#다른 코드
def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:])
        arr2_bin.append(bin(arr2[i])[2:])
        arr1_bin[i] = ('0' * (n-len(arr1_bin[i]))) + arr1_bin[i]
        arr2_bin[i] = ('0' * (n-len(arr2_bin[i]))) + arr2_bin[i]
        tmp = ''
        for j in range(n):
            if arr1_bin[i][j] == '1' or arr2_bin[i][j]=='1':
                tmp+='#'
            else:
                tmp+=' '
        answer.append(tmp)
    return answer

'''
#Remind
1. 2진수로 만들 때에는 bin() 함수를 사용한다.
bin(9) = 	0b1001
bin(9)[2:] = 1001

2. 원래 내 답에서는 하나하나 step을 나눠서 여러개의 for문을 써서 풀엇는데 
다른 코드에서는 행마다 모든 연산을 수행하여 마무리하도록 풀었다(for의 갯수가 많지 않음:2중 for문 1개 나는 2중 for문 2개와 for문 2개).
이렇게 풀 수 있다는 것도 알아두자.
'''