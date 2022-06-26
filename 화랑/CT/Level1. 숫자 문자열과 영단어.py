def solution(s):
    answer = 0
    code = ['zero', 'one', 'two', 'three','four','five','six','seven','eight','nine']
    for i,j in enumerate(code):
        s = s.replace(j,str(i))
    answer = int(s)
    return answer