def solution(progresses, speeds):
    answer = []
    check = [1 for i in range(len(speeds))] # 0:배포완료, 1:배포미완료
    count = 0
    index = 0 # 이미 확인했던 index 방지하기 위함
    while 1:
        if sum(check)==0: # check 배열의 합이 0이면 모든 기능 배포 완료
            break
        for i in range(len(speeds)): # 작업 진행 반복문
            progresses[i] += speeds[i]
        for i in range(index, len(speeds)):
            if progresses[i]>=100: # 배포가능한 경우
                check[i]=0
                count += 1
                index = i+1
            else: # 배포 불가능
                break
        if count != 0:
            answer.append(count)
        count = 0
    return answer