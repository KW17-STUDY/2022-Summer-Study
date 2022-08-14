def convertToSec(hour, minute, sec):
    return (hour*60*60 + minute*60 + sec)*1000
    
def solution(lines):
    infos = []
    answer = 0
    for line in lines:
        _, time, throughput = line.split(' ')
        hour, minute, sec = time.split(':')
        throughput = list(throughput)
        throughput.remove('s')
        throughput = ''.join(throughput)
        hour, minute = int(hour), int(minute)
        sec, throughput = float(sec), float(throughput)
        end_time = convertToSec(hour, minute, sec)
        start_time = end_time - throughput*1000 + 1
        infos.append([start_time, end_time])
    for i in range(len(infos)):
        cnt = 0
        cur_end_time = infos[i][1]
        for j in range(i, len(infos)):
            if cur_end_time > infos[j][0] - 1000:
                cnt += 1
        answer = max(answer, cnt)
        
    return answer
        
#참고 코드
def solution(lines):
    answer = 0
    start_time = []
    end_time = []

    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1