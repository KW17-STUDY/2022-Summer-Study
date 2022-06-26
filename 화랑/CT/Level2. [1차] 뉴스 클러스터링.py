from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha(): # 알파벳만 거르기
            arr1.append(str1[i] + str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha(): # 알파벳만 거르기
            arr2.append(str2[j] + str2[j+1])
            
    if len(arr1) == 0 and len(arr2) == 0: # 공집합인 경우
        return 65536
    
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    
    aggre = sum((c1 | c2).values())
    inter = sum((c1 & c2).values())

    return int(inter / aggre * 65536)