num = 0
if num:
    print('True')
else:
    print('false')

num = 1
if num:
    print('True')
else:
    print('false')

num = -1
if num:
    print('True')
else:
    print('false')

num = None
if num:
    print('True')
else:
    print('false')
print('-------------')
name_dict = {'ant': 'small', 'elephant': 'big'}
if 'ant' in name_dict:
    print(True)
else:
    print(False)

if 'big' in name_dict:
    print(True)
else:
    print(False)
print('-------------')
for i in name_dict:
    print(i)

'''
1. if 문에서 0, None, False가 들어가게 되면 실행되지 않는다. -1이나 1은 True로 인식한다.
2. dict는 key를 통해서만 접근가능하다. key값이 있는지 없는지만 검사 할 수 있고 value 값은 독립적으로 검사 불가능. 반드시
key값을 통해서만 접근해야 한다.
'''
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(max(map(max,a)))

from collections import deque

q = deque([1,2,3])
q.append(1)
print(q) #[1,2,3,1]

q.pop()
print(q) #[2,3,1]


from itertools import combinations

num_list = [1,2,3,4,5]
comb = list(combinations(num_list, 2))
print(len(comb)) #5C2 = 10
print(comb) 
#[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

from itertools import combinations_with_replacement

num_list = '12345'
result = list(combinations_with_replacement(num_list, 2))
print(len(result)) 
# 5C2+5(자기 자신을 2번 뽑은 경우) = 15

print(result)

from itertools import permutations

num_list = '12345'
result = list(permutations(num_list, 2))
print(len(result))

print(result)

from itertools import product

num_list = [1,2,3,4,5]
result = list(product(num_list, repeat=2))
print(len(result))
# 5π2 = 25

print(result)


from collections import Counter

num_list = [1,2,2,3,3,3,4,4,4,4,5]
counter = Counter(num_list)
print(counter)

num_string = 'hello world'
counter = Counter(num_string)
print(counter)

from collections import defaultdict

person_dict = defaultdict(int)
person_dict['muji'] = 3
person_dict['peach'] += 1 
# 자동적으로 person_dict['peach']의 값이 0으로 초기화되어 1이 저장

print(person_dict)