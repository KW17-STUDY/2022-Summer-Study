import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계 소문자로 변경
    new_id = re.sub('[^0-9a-z-_.]','',new_id) # 2단계 정규식 사용 특정 문자만 유지
    new_id = re.sub('(([.])\\2{1,})', '.', new_id) # 3단계 연속 마침표 제거
    new_id = new_id.strip('.') # 4단계 양쪽 . 제거
    if new_id=='':
        new_id+='a' # 5단계 a 대입
    if len(new_id)>=16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.') # 6단계 우측 . 제거
    if len(new_id)<=2:
        temp = new_id[len(new_id)-1:]
        while len(new_id)!=3:
            new_id+=temp # 7단계 반복 추가

    answer = new_id
    return answer