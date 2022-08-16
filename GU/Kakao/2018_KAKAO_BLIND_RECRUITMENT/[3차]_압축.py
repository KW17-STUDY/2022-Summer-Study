#58분

from collections import defaultdict

def solution(msg):
    answer = []
    
    # dict 초기화
    dictionary = defaultdict(int)
    for idx, alpha in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        dictionary[alpha] = idx+1
    print(dictionary.keys())
    
    # dict 만들기
    i = 0
    while i < len(msg):
        end = i+1
        while True:
            if end-1 >= len(msg):
                if msg[i:end] not in dictionary.keys():
                    dictionary[msg[i:end]] = max(dictionary.values())+1
                    answer.append(dictionary[msg[i:end-1]])
                    i+=(end-1-i)
                    break
                else:
                    answer.append(dictionary[msg[i:end]])
                    i+=(end-i)
                    break
            if msg[i:end] not in dictionary.keys():
                dictionary[msg[i:end]] = max(dictionary.values())+1 
                answer.append(dictionary[msg[i:end-1]])
                i+=(end-1-i)
                break
            else:
                end+=1
    return answer

#다른 답
#58분
def solution(msg):
    d = dict()
    for i in range(65, 91):
        d[chr(i)] = i-64
    start = 0
    end = len(msg)
    r = []
    
    while True:
        a = msg[start:end]
        if a in d.keys():
            r.append(d[a])
            
            if end >= len(msg): # end==len(msg)도 가능
                return r
            d[a+msg[end]] = max(d.values())+1
            start += len(a)
            end = len(msg)
        else:
            end -=1
    return answer
    '''
    끝에서부터 end를 하나씩 줄여가면서 dict안에 들어있는지 안들어있는지 검사한 이후, 들어간걸 찾을 때 까지 end를 줄인다.
    dict에 있는 것을 찾게되면 그다음에 존재하는 단어까지 포함해서(a+msg[end]) dict에 등록한 이후 start와 end를 다시 조정한다.
    '''

    '''
    #Remind
    1. slicing할 때 [start:end]이면 end-1까지 접근하는데 바로 접근할 때 [end]로하면 해당 index에 바로 접근하므로
    헷갈리지 말기.

    2. 'A' 아스키코드 값: 65 'a' 아스키 코드값:97
    chr(97)을 통해 int에서 문자로 변환 가능하다.
    '''