n = input()
length = len(n)

# 짜를 단위를 설정
final_result = []
min_len = length

# 묶을 단위의 범위: 1 ~ 절반
for i in range(1, length//2+1):
    # i만큼의 묶음으로 받아서 검사하기
    # 연속된 문자열의 개수를 세어주는 count
    count = 0
    # 이전 string
    prev_str = ''
    # 결과 값을 담는 result
    result = []
    for j in range(0, length, i):
        part_string = n[j:j+i]
        print('부분 str: ', part_string)
        # 초기 상태일 때는 prev_str이 없으므로 바로 다음으로 넘어갈 수 있도록 예외처리
        if j == 0:
            prev_str = part_string
            count += 1
            continue
        # 이전 str과 현재 str이 같다면 +1
        print('prev_str:', prev_str, 'str:', part_string)
        if prev_str == part_string:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
                count = 1
            result.append(prev_str)
        #print('count:', count)
        print('result:', result)
        prev_str = part_string
    # 마지막 부분 처리
    if count > 1:
        result.append(str(count))
    result.append(part_string)
    print(result)
    if min_len > len(''.join(result)):
        final_result = result
        min_len = len(''.join(result))

print('final_result:', ''.join(final_result))
print('answer:', min_len)


# Another answer
def solution(s):
    answer = len(s)
    # step 범위: 1 ~ 절반
    for step in range(1, len(s)//2+1):
        # 압축된 문자열 저장
        compressed = ""
        # 이전 string을 처음껄로 초기화
        prev = s[0:step]
        # count 1로 초기화
        count = 1

        # 이전 string을 처음껄로 초기화 했으므로 step부터 시작
        for j in range(step, len(s), step):
            # 이전 string과 현재의 string이 같다면 count만 올리기
            if prev == s[j:j+step]:
                count += 1
            # 다르다면 이전 string을 count를 고려해서 압축된 문자열에 추가
            # + 연산자 사용
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


'''
# Remind
1. string을 slicing해서 이전의 string과 ==을 통해 비교.
2. 문자열을 통해 어떤 처리를 해줄 땐 list에 넣어서 처리(element들 재조합 등등)해주고(=> 해답에선 +연산자를 이용해서 조합)
단순 slicing을 통한 비교를 하는건 문자열이 편하다.
3. 17행의 part_string = n[j:j+i]에서 j+i가 배열의 크기를 넘어가도 마지막 배열의 element까지만 slicing된다.
4. 문자열에 문자열을 덧붙일 땐 + 연산자 사용
'''
