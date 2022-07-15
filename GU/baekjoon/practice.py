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
