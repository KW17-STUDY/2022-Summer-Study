# 제출 코드
def solution(n, k):
    answer = 0
    cvt_str, remain = '', ''
    while k<= n:
        remain=str(n%k)
        n //=k
        cvt_str = remain + cvt_str
    cvt_str = str(n) + cvt_str

    prime_list = cvt_str.split('0')
    for i in prime_list[:]:
        if i =='':
            prime_list.remove('')
        if i =='1':
            prime_list.remove('1')
    prime_list = list(map(int, prime_list))
    
    flag = True
    for i in prime_list:
        for j in range(2,int(i**0.5+1)):
            if i%j == 0:
                flag = False
                break
        if flag==True:
            answer += 1
        flag = True
    return answer



# Code 정리
def convert(n, k):
    cvt_str = ''
    # n을 k진수로 변환
    while n > 0:
        n, remain = divmod(n, k)
        cvt_str = str(remain) + cvt_str
    return cvt_str

def getPrimeNum(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True
    

def solution(n, k):
    cvt_str = convert(n,k)
    prime_list = cvt_str.split('0')
    prime_list = list(filter(lambda x: x!='', prime_list))
    prime_list = list(map(lambda x: getPrimeNum(int(x)),prime_list))
    return prime_list.count(True)
'''
#Remind
1. divmod(나눠질 값, 나누는 값)
divmod(10,3) => (3,1) # 몫, 나머지
divmod(1,3)  => (0,1) 

2. filter(함수, 리스트)
list(filter(lambda x: x!='', list))
=> 리스트인 list안에서 ''인 원소 필터링하여 list만들기

3. map(함수, 리스트)
list(map(lambda x: getPrimeNum(x), list))
=> 함수도 map안에 적용 가능

4. list.count('갯수를 세고 싶은 원소 이름')
list.count(True) => True의 개수를 세줌
'''