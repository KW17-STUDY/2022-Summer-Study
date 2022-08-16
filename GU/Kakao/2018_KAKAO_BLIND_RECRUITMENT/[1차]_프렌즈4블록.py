#35분
def printGrid(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
        
def slideWindow(m,n,board):
    num = 0
    while True:
        coord = []
        # 케릭터가 같은 위치 찾기
        for i in range(m-1):
            for j in range(n-1):
                # 첫 블록이 0이면 다음 블록으로..
                if board[i][j] == 0:
                    continue
                init_block = board[i][j]
                flag = True
                #블록 생성
                for r in range(i, i+2):
                    for c in range(j, j+2):
                        if init_block != board[r][c]:
                            flag = False
                if flag == True:
                    coord.append((i,j))
        if len(coord) == 0:
            break
        # 해당 위치를 0으로 만들면서 0 갯수 세주기
        for (x,y) in coord:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    if board[i][j] != 0:
                        num+=1
                        board[i][j] = 0
    
        # 내려주기
        new_board = [[0 for _ in range(n)]for _ in range(m)]
        for j in range(n):
            n_idx = m-1
            for i in range(m-1,-1,-1):
                if board[i][j] != 0:
                    new_board[n_idx][j] = board[i][j]
                    n_idx-=1
        board = new_board
    return num, board
def solution(m, n, board):
    total_cnt = 0
    list_board = []
    for row in board:
        list_board.append(list(row))
    board = list_board
    cnt, board = slideWindow(m,n,board)
    total_cnt+=cnt
    return total_cnt
'''
#Remind
1. 내려줄 때, 새로운 리스트 사용해서 0이 아니면 차례대로 대입시켜주기.
위에서 아래로 내려오는 '중력'같은 것들을 구현할 때, 새로운 리스트를 선언해서
원래의 리스트로부터 0이 아닌것을 새로운 리스트에 아래에서 부터 차례대로 
대입시켜주면 된다.
'''
