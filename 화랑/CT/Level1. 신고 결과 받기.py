from collections import defaultdict

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report = set(report) # 중복 신고 제거
    reportList = defaultdict(set) # 신고한사람 : 신고당한사람
    count = defaultdict(int) # 신고당한사람 : 횟수

    for pair in report:
        a, b = pair.split()
        reportList[a].add(b)
        count[b] += 1
        
    for user in id_list:
        for badguy in reportList[user]:
            if count[badguy] >= k:
                answer[id_list.index(user)] += 1
    
    return answer