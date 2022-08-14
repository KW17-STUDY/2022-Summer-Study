prac = 'a1'
print(prac.isalpha())
prac = 'aa'
print(prac.isalpha())

from collections import Counter
str1 = 'aa1+aa2'
str2 = 'AAAA12'

answer = 0
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

