#7:48~8:24
#36분
import re
from collections import defaultdict
def solution(files):
    answer = []
    file_dict = defaultdict(str)
    #추출
    for file in files:
        HEAD = re.search('([^0-9]+)',file).group(1)
        NUMBER = re.findall('([0-9]+)',file)
        #NUMBER = re.search('([0-9]+)',file).group(1)도 가능
        temp= file.replace(HEAD,'')
        TAIL = temp.replace(NUMBER[0],'')
        file_dict[file] = [HEAD, int(NUMBER[0]), TAIL]
    files = sorted(list(file_dict.keys()), key = lambda x: [file_dict[x][0].lower(), file_dict[x][1]])
    return files

#내 코드 정리
import re
from collections import defaultdict 

def solution(files):
    answer = []
    file_dict = defaultdict(str)
    #추출
    for file in files:
        HEAD = re.search('(\D+)',file).group(1) #숫자가 아닌 것:\D
        NUMBER = re.search('(\d+)',file).group(1) #숫자 인 것:\D
        temp= file.replace(HEAD,'')
        TAIL = temp.replace(NUMBER,'')
        file_dict[file] = [HEAD, int(NUMBER), TAIL]
    
    files = sorted(file_dict.items(), key = lambda x: [x[1][0].lower(), x[1][1]])
    print(file_dict.items())
    
    return [file[0] for file in files]

#다른 사람 코드 
def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)): # 문자열 자르기
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += f[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬

    return [''.join(t) for t in answer]   # 원래 형태로 문자열 만들어서 반환
'''
#Remind
1. dict를 sort하는 부분을 아래와 같이 바꿀 수 있다.
files = sorted(file_dict.items(), key = lambda x: [x[1][0].lower(), x[1][1]]) #x[1][0]:value의 HEAD를 의미. x[1][1]:value의 NUMBER를 의미
return [file[0] for file in files]

file_dict.items()를 print해보면 아래와 같이 value와 key가 튜플형태로 모아진 list로 나오게 된다.
file_dict.items(): 
dict_items([('img12.png', ['img', 12, '.png']), ('img10.png', ['img', 10, '.png']), ('img02.png', ['img', 2, '.png']),
('img1.png', ['img', 1, '.png']), ('IMG01.GIF', ['IMG', 1, '.GIF']), ('img2.JPG', ['img', 2, '.JPG'])])

2. 다른 사람들 코드는 isdigit을 통해 구현하였다.
파이썬에는 isalpha(),isdigit(),isalnum()이 존재한다.
'''