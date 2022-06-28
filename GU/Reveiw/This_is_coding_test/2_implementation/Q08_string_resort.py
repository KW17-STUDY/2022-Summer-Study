input_string = input()

sum_num = 0
resort_string = []
for i in input_string:
    if i.isalpha():
        resort_string.append(i)
    else:
        sum_num += int(i)

resort_string.sort()
if i != 0:
    resort_string.append(str(sum_num))
print(''.join(resort_string))

'''
# Remind
1. 문자열로 만들기 전에 list에서 처리하기
문자열로 만들기 전에 list에 넣고 처리해주고 마지막에 ''.join(list) 사용해서 문자열로 만들기
2. i.isalpha()
input으로 받은 문자열을 for문에 넣어 하나씩 뽑아주고 뽑아낸 문자열 하나하나마다 isalpha()를 적용해서
알파벳인지 숫자인지 검사하기
'''
