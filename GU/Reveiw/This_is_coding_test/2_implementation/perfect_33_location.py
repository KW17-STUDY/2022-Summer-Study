# My answer

n = int(input())

grid = [
    list(map(int, input().split())) for i in range(n)
]


def in_range(x, y):
    return x < n and x >= 0 and y < n and y >= 0


def check_coin_num(x, y):
    num = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if grid[i][j] == 1:
                num += 1
    return num


maximum_coin_num = 0
for row in range(n):
    for col in range(n):
        # grid 범위 안에 있는지 검사
        # 범위 안에 없다면:
        if not in_range(row+2, col+2):
            continue
        # 범위 안에 있으면
        coin_num = check_coin_num(row, col)
        maximum_coin_num = max(coin_num, maximum_coin_num)

print(maximum_coin_num)
###################################################################
# Another answer
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def get_num_of_gold(row_s, col_s, row_e, col_e):
    return sum([
        grid[i][j]
        for i in range(row_s, row_e + 1)
        for j in range(col_s, col_e + 1)
    ])


max_gold = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= 2 or col + 2 >= n:
            continue
        num_of_gold = get_num_of_gold(row, col, row+2, col+2)
        max_gold = max(num_of_gold, max_gold)
print(max_gold)

'''
# Remind
1. 2차원 배열 초기화
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
    (1) 단순히 반복하기 위해 반복문 돌릴 땐 _ 사용
    (2) input()은 str로 저장되기 때문에 모든 배열에 있는 str을 int로 만들어 줄 떄 map사용

2. 2차원 배열의 일부분 가져오기
def  get_num_of_gold(row_s, col_s, row_e, col_e):
    return sum([
        grid[i][j]
        for i in range(row_s, row_e+1)
        for j in range(col_s, col_e+1)
    ])
    (1) 2차원 배열의 일부분을 가져와서 
    (2) sum하여 fancy하게 coin의 갯수 세기
'''
