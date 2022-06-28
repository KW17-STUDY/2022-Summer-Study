def solution(record):
    answer = []
    user = {}
    for com in record:
        com = com.split()
        if com[0]=='Enter' or com[0]=='Change':
            user[com[1]] = com[2]
    for com in record:
        com = com.split()
        if com[0]=='Enter':
            answer.append(f'{user[com[1]]}님이 들어왔습니다.')
        elif com[0]=='Leave':
            answer.append(f'{user[com[1]]}님이 나갔습니다.')
    
    return answer