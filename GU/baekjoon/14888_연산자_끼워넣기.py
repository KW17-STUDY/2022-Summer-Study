import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
tools = list(map(int, input().split()))
INF = 1e9
max_num = -INF
min_num = INF


def recursive(depth, value):
    global max_num, min_num
    if depth == len(num_list)-1:
        max_num = max(max_num, value)
        min_num = min(min_num, value)
        return
    for i in range(4):
        # 덧셈
        if i == 0 and tools[0] > 0:
            origin_val = value
            value += num_list[depth+1]
            tools[0] -= 1
            recursive(depth+1, value)
            tools[0] += 1
            value = origin_val
        # 뺄셈
        elif i == 1 and tools[1] > 0:
            origin_val = value
            value -= num_list[depth+1]
            tools[1] -= 1
            recursive(depth+1, value)
            tools[1] += 1
            value = origin_val
        # 곱셈
        elif i == 2 and tools[2] > 0:
            origin_val = value
            value *= num_list[depth+1]
            tools[2] -= 1
            recursive(depth+1, value)
            tools[2] += 1
            value = origin_val
        # 나눗셈
        elif i == 3 and tools[3] > 0:
            origin_val = value
            if value < 0:
                temp = -value / num_list[depth+1]
                value = -int(temp)
            else:
                value /= num_list[depth+1]
                value = int(value)
            tools[3] -= 1
            recursive(depth+1, value)
            tools[3] += 1
            value = origin_val
        else:
            pass


recursive(0, num_list[0])
print(max_num)
print(min_num)


# 다른 사람 코드

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]),
            plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

"""
# Remind
1. dfs에서 인자에 계산 자체를 넣어주면 해당 재귀함수가 끝난 이후에 빼주지 않아도 되기 때문에
편리하다. 내 코드에선 값들을 복구시키기 위해서 빼주었는데 다른 답변에서는 파라미터로 계산식을
넣어서 간소화 했다.
내 코드에서 사칙연산 계산과 operation의 남은 갯수를 check하는 2개의 부분을 파라미터에 계산식을 넣는 것을 통해
없애서 간소화 가능하다.
"""
