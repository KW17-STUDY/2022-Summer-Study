from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    fired = []
    reporting_info = defaultdict(list)
    reported_info = defaultdict(int)
    result_mail = defaultdict(int)
    # 중복 신고 제거
    report = list(set(report))
    
    # 신고한 내역 및 신고당한 횟수
    for infos in report:
        reporting, reported = infos.split()
        reporting_info[reporting].append(reported)
        reported_info[reported] += 1
    
    # 정지 되어야할 명단
    for i in reported_info:
        if reported_info[i] >= k:
            fired.append(i)
    
    # 처리 결과 메일을 받아야할 횟수
    for i in fired:
        for j in reporting_info:
            if i in reporting_info[j]:
                result_mail[j] += 1
    for i in id_list:
        answer.append(result_mail[i])
    
    return answer

# Code 정리
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    reporting_info = defaultdict(list)
    reported_info = defaultdict(int)
    # 중복 신고 제거
    report = list(set(report))
    
    # 신고한 내역 및 신고당한 횟수
    for infos in report:
        reporting, reported = infos.split()
        reporting_info[reporting].append(reported)
        reported_info[reported] += 1
    
    for i in id_list:
        result = 0
        for j in reporting_info[i]:
            if reported_info[j]>=k:
                result += 1
        answer.append(result)
    return answer
'''
# Remind
1. defualtdict
2. fired와 result_mail을 안쓰고 구현할 수 있다.
id_list를 순서대로 받아 신고자가 신고한 피신고자의 신고 횟수를 받아 검사하여
answer에 처리 메이을 몇번 받는지 추가하는 방식으로 구현하면 된다.
'''
