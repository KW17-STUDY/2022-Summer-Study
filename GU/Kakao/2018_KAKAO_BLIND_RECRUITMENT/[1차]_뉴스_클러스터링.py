from collections import defaultdict

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    str1_list = []
    str2_list = []
    for i in range(1, len(str1)):
        part = ''.join([str1[i-1],str1[i]])
        if part.isalpha():
            str1_list.append(part)
            
    for i in range(1, len(str2)):
        part = ''.join([str2[i-1],str2[i]])
        if part.isalpha():
            str2_list.append(part)
    
    str1_dict, str2_dict = defaultdict(int), defaultdict(int)
    
    for i in str1_list:
        str1_dict[i] += 1
        
    for i in str2_list:
        str2_dict[i] += 1
    
    temp = []
    total = []
    inter = []
    temp.extend(str1_dict.keys())
    temp.extend(str2_dict.keys())
    temp = set(temp)
    temp = list(temp)
    print(str1_dict, str2_dict)
    for i in temp:
        if i in str1_dict.keys() and i in str2_dict.keys():
            for j in range(min(str1_dict[i], str2_dict[i])):
                inter.append(i)
            for j in range(max(str1_dict[i], str2_dict[i])):
                total.append(i)
        else:
            if i in str1_dict.keys():
                for j in range(str1_dict[i]):
                    total.append(i)
            if i in str2_dict.keys():
                for j in range(str2_dict[i]):
                    total.append(i)
                
    if len(total) == 0:
        answer = 65536
    else:
        answer = int(len(inter)/len(total)*65536)
    return answer

# 재구성

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    str1_list, str2_list = [], []

    for i in range(1, len(str1)):
        part = str1[i-1]+str1[i]
        if part.isalpha():
            str1_list.append(part)
            
    for i in range(1, len(str2)):
        part = str2[i-1]+str2[i]
        if part.isalpha():
            str2_list.append(part)
    
    str1_dict, str2_dict = defaultdict(int), defaultdict(int)
    
    for i in str1_list:
        str1_dict[i] += 1
        
    for i in str2_list:
        str2_dict[i] += 1
    
    temp = []
    total = []
    inter = []
    temp.extend(str1_dict.keys())
    temp.extend(str2_dict.keys())
    temp = list(set(temp))
    for i in temp:
        if i in str1_dict.keys() and i in str2_dict.keys():
            for j in range(min(str1_dict[i], str2_dict[i])):
                inter.append(i)
            for j in range(max(str1_dict[i], str2_dict[i])):
                total.append(i)
        else:
            if i in str1_dict.keys():
                for j in range(str1_dict[i]):
                    total.append(i)
            if i in str2_dict.keys():
                for j in range(str2_dict[i]):
                    total.append(i)
                
    if len(total) == 0:
        answer = 65536
    else:
        answer = int(len(inter)/len(total)*65536)
    return answer

# 다른분 답
from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

#다른분 답
from math import floor

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(str2[i:i + 2])

    intersection_list = set(str1_list) & set(str2_list)
    union_list = set(str1_list) | set(str2_list)

    if len(union_list) == 0:
        return 65536

    intersection_len = sum([min(str1_list.count(intersection), str2_list.count(intersection)) for intersection in intersection_list])
    union_len = sum([max(str1_list.count(union), str2_list.count(union)) for union in union_list])

    answer = floor((intersection_len / union_len) * 65536)

    return answer
    '''
# Remind
1. 교집합, 차집합, 합집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2 => 교집합({4, 5, 6})
s1 | s2 => 합집합({1, 2, 3, 4, 5, 6, 7, 8, 9})
s1 - s2 => 차집합({1, 2, 3})

2. Counter 또한 &이나 |를  사용 가능.

Counter1 = Counter(str1_lst)
Counter2 = Counter(str2_lst)

print('Counter1:',Counter1)
print('Counter2:',Counter2)

inter = list((Counter1 & Counter2).elements())
print(Counter1&Counter2)
print((Counter1&Counter2).elements())
print(list((Counter1&Counter2).elements()))

union = list((Counter1 | Counter2).elements())
print(Counter1 | Counter2)
print((Counter1 | Counter2).elements())
print(list((Counter1 | Counter2).elements()))
```
Counter1: Counter({'aa': 2})
Counter2: Counter({'aa': 3})
Counter({'aa': 2})
<itertools.chain object at 0x00000256644E3FD0>
['aa', 'aa']
Counter({'aa': 3})
<itertools.chain object at 0x00000256644E3FD0>
['aa', 'aa', 'aa']
```
'''