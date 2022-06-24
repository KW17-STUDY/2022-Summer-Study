def solution(s):
    answer = 100000
    for i in range(1,len(s)//2+2): # 1~ 차례대로 자르는 단위 설정
        a = ''
        count = 1
        temp = s[:i] # 앞부터 잘라야 하므로 미리 자르기
        for j in range(i,len(s)+i, i):
            if temp==s[j:j+i]: # 잘랐던거랑 똑같은거 나오면 count 증가
                count += 1
            else: # 다른거 나오면 문자열 만들어주기
                if count!=1: # 앞에서 중복이 O 경우
                    a += str(count)+temp # 숫자 포함해서 문자열 만들어줌
                else: # 앞에서 중복이 X 경우
                    a += temp # 숫자 포함하지 않고 문자만 추가
                temp = s[j:j+i] # 슬라이싱 갱신
                count = 1 # 카운트 초기화
        answer = min(answer, len(a)) # 가장 짧았던 길이 갱신
    return answer