#내 답
def removeChar(string):
    tmp = ''
    dot_cnt = 0
    for s in string:
        if not (s.isalpha() or s.isdigit() or s=='-' or s =='_' or s=='.'):
            continue
        tmp += s
    return tmp[:]
def changeDot(string):
    tmp = ''
    dot_cnt = 0
    for s in string:
        if s == '.':
            if dot_cnt ==1:
                continue
            else:
                dot_cnt+=1
                tmp+=s
        else:
            dot_cnt = 0
            tmp+=s
    return tmp[:]

def removeDotSE(string):
    if len(string) ==1:
        if string[0] == '.':
            return ''
    else:
        if string[0] == '.':
            string = string[1:]
        if string[-1] == '.':
            string = string[:-1]
    return string    

def solution(new_id):
    new_id = new_id.lower()
    new_id = removeChar(new_id)
    new_id = changeDot(new_id)
    new_id = removeDotSE(new_id)
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = removeDotSE(new_id)
    if len(new_id) <= 2:
        while len(new_id)<3:
            new_id+=new_id[-1]
    return new_id