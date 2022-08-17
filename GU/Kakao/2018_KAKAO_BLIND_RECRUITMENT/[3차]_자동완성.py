#link:https://school.programmers.co.kr/learn/courses/30/lessons/17685
#09:05~09:20
#15분
#정확성: 68.2
#합계: 68.2 / 100.0
#시간 초과
import re
def check(part, words, cur_word):
    #print(part,'와 비교합니다.')
    for word in words:
        #입력 중인 단어와는 비교 skip
        if cur_word == word:
            continue
        #겹치는 문제가 있으므로 하나를 더 입력 해야함
        if re.match(part,word) is not None:
            #print('겹칩니다')
            return False
    #print('겹치지 않습니다')
    return True
def solution(words):
    answer = 0
    for word in words:
        #print(word)
        partial_word = ''
        for alpha in word:
            partial_word += alpha
            answer+=1
            # False면 하나를 더 입력 해야하므로 continue
            if not check(partial_word, words, word):
                continue
            else:
                break
        #print('누적 cnt:',answer)
    return answer

#고친 코드 
def solution(words):
    answer = 0
    start_point = 0
    prev_cnt = 0
    words = sorted(words)
    for i in range(len(words)):
        if i == 0:
            for j in range(len(words[i])):
                if j<len(words[i+1]): 
                    answer += 1
                    if words[i][j] != words[i+1][j]:
                        break
                else:
                    answer += 1
                    break   
        elif i==len(words)-1:
            for j in range(len(words[i])):
                if j<len(words[i-1]): 
                    answer += 1
                    if words[i][j] != words[i-1][j]:
                        break
                else:
                    answer += 1
                    break     
        else:
            temp1, temp2= 0, 0
            for j in range(len(words[i])):
                if j<len(words[i-1]): 
                    temp1 += 1
                    if words[i][j] != words[i-1][j]:
                        break
                else:
                    temp1 += 1
                    break
            for j in range(len(words[i])):
                if j<len(words[i+1]): 
                    temp2 += 1
                    if words[i][j] != words[i+1][j]:
                        break
                else:
                    temp2 += 1
                    break   
            answer += max(temp1, temp2)
    return answer

"""
#Remind
1. 처음엔 간단하게 풀었는데 시간초과가 났다.
이유는 단어의 개수가 10만개이고 단어의 길이가 100만개여서 단어의 길이와 단어의 갯수로 이중 for문을
작성하면 시간초과가 난다. O(n*m) = 1000억번의 연산이 필요하기 때문이다.
이에 nlogn을 사용하는 sort를 사용해야하는지 생각했고 sorting을 통해 문제를 해결했다.
"""