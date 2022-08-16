#1:30

def calTime(time, end):
    hour = int(end[0])-int(time[0]) 
    minute = int(end[1]) - int(time[1])
    if minute < 0:
        hour -= 1
        minute += 60
    spend_time = hour * 60 + minute
    return spend_time
    
def solution(m, musicinfos):
    max_play_time = 0
    answer = ''
    for musicinfo in musicinfos:
        [start, end, title, alpha] = musicinfo.split(',')
        time, end = start.split(':'), end.split(':')
        spend_time = calTime(time, end)
        origin_alpha = []
        idx = 0
        walker = spend_time
        #재생된 악보 list로 구성
        while walker != 0:
            if idx == len(alpha):
                idx = idx % len(alpha)
            origin_alpha.append(alpha[idx])
            walker -= 1
            if idx+1 < len(alpha) and alpha[idx+1] == '#':
                origin_alpha[-1] = origin_alpha[-1]+'#'
                idx+=2
            else:
                idx+=1
        m_list = []
        idx = 0
        #네오가 들은 악보 list로 구성
        for i in range(len(m)):
            if m[i] == '#':
                m_list[len(m_list)-1] = m_list[len(m_list)-1] + '#'
            else:
                m_list.append(m[i])
        
        #악보 비교
        for o_idx, o_alpha in enumerate(origin_alpha):
            if m_list[0] == o_alpha:
                #print('find')
                for i in range(len(m_list)):
                    if o_idx + i >=len(origin_alpha):
                        break
                    #print(m_list[i], origin_alpha[o_idx+i])
                    if m_list[i] != origin_alpha[o_idx+i]:
                        break
                else:
                    if max_play_time < spend_time:
                        max_play_time = spend_time
                        answer = title
                        break
        if answer == '':
            answer = "(None)"
    return answer

#다른 답
import math

def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")
        
        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute
        
        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start
        
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        code *= math.ceil(duration / len(code))
        code = code[:duration]
        
        if m not in code:
            continue
            
        if answer == None or answer[0] < duration:
                answer = (duration, start, title)
    
    if answer:
        return answer[-1]
    
    return "(None)"
'''
Remind
1. 하나씩 넘기면서 #인지 알파벳인지 검사하는 것 보다는 현재가 알파벳일 때 다음 인덱스에 있는 것이 #인지 검사하는 로직이
오류가 없도록 작동한다.

이전 코드 오류가 났던 테스트 케이스 :
입력값 〉	"A#", ["13:00,13:02,HAPPY,B#A#"]
기댓값 〉	"HAPPY"
실행 결과 〉	실행한 결괏값 "(None)"이 기댓값 "HAPPY"과 다릅니다.

오류 났던 코드:
while walker != 0:
    if idx == len(alpha):
        idx = idx % len(alpha)
        print('idx')
    print('value: ',alpha[idx])
    print('walker":',walker)
    if alpha[idx] != '#':
        origin_alpha.append(alpha[idx])
        walker -= 1
        idx += 1
    else:
        origin_alpha[len(origin_alpha)-1] = origin_alpha[len(origin_alpha)-1]+'#'
        idx += 1

오류가 난 이유: 시간이 2초동안이라 walker의 값이 2이기 때문에 (B#,A#)을 잡지 않고 (A#,B)로 잡았다.
B를 검사하기 전 walker는 2, #을 검사하기 전  walker는 1, A를 검사하기 전  walker는 1이 되어 A까지 검사하고 난 walker는 0이 되므로
반복문에 들어가지 않아 #을 검사하지 않는다.
이런 경우, 알파벳을 받았을 때 다음 인덱스에 존재하는 것이 #인지 검사하는 것이 오류가 없다.

2. for ... else...
for문이 중간에 break등으로 끊기지 않고 끝까지 수행 되었을 때 else에 존재하는 코드를 수행한다.

3.시간 계산할 때 분으로 변환 후 계산
이전 문제에서도 분으로 변환한 이후 계산한 것이 빠른데 시간끼리 뺴주고 분끼리 뺴줘서 계산하였다.
앞으로는 분으로 변환 후 바로 계산하자.

4. 내코드는 재생 시간만큼 whle문을 반복해서 재생된 악보를 작성해주었지만 다른 사람 답에서는 (재생된 시간/악보의 길이)를 계산(math.ceil(duration / len(code)))하여
그만큼 반복해주었다. 이후, duration만큼 slicing해서 실제 재생된 악보를 작성하였다. 코드 상으로 다른 사람의 답이 간단하니 해당 코드를 참고하자.

5. 특정 패턴이 반복되는 경우, 치환을 사용한다.
치환을 사용하게 되면 간단하게 구현할 수 있다.
'''