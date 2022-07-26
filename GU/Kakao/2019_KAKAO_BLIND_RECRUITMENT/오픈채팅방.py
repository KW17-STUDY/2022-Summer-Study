def solution(record):
    answer = []
    name_dict = {}
    for i in record:
        record_object_list = i.split()
        if record_object_list[0] == 'Enter' or record_object_list[0] == 'Change':
            name_dict[record_object_list[1]] = record_object_list[2]
    for string in record:
        commands = list(string.split())
        command, uid = commands[0], commands[1]
        if command == 'Enter':
            answer.append(name_dict[uid]+"님이 들어왔습니다.")
        if command == 'Leave':
            answer.append(name_dict[uid]+"님이 나갔습니다.")
    return answer
