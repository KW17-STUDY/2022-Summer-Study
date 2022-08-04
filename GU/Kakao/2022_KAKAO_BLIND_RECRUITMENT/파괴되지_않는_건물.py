# 정확성 테스트 통과
# 효율성 테스트 불통
# O(250,000 * 1000 * 1000 => 250,000,000,000) : 시간 초과
def attack(board, attack_type, r1, c1, r2, c2, degree):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if attack_type==1:
                board[i][j]-=degree
            if attack_type==2:
                board[i][j]+=degree
    return board
def count_valid(board):
    result = 0
    rows, cols = len(board), len(board[0])
    print(cols, rows)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] > 0:
                result+=1
    return result

def solution(board, skill):
    for attack_type, r1, c1, r2, c2, degree in skill:
        board = attack(board, attack_type, r1, c1, r2, c2, degree)
    answer = count_valid(board)
    return answer

# imos 알고리즘 사용(누적합 알고리즘)
def solution(board, skill):
    answer = 0
    rows, cols = len(board), len(board[0])
    imos = [[0 for _ in range(cols+1)]for _ in range(rows+1)]
    for attack_type, r1, c1, r2, c2, degree in skill:
        imos[r1][c1] += -degree if attack_type == 1 else degree
        imos[r1][c2+1] += degree if attack_type == 1 else -degree
        imos[r2+1][c1] += degree if attack_type == 1 else -degree
        imos[r2+1][c2+1] += -degree if attack_type == 1 else degree
    
    for i in range(len(imos)):
        for j in range(1, len(imos[0])):
            imos[i][j]+=imos[i][j-1]
    for j in range(len(imos[0])):
        for i in range(1, len(imos)):
            imos[i][j]+=imos[i-1][j]
    
    for i in range(rows):
        for j in range(cols):
            imos[i][j] += board[i][j]
            if imos[i][j] > 0:
                answer+=1
    return answer