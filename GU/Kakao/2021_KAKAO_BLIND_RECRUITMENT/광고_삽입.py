import sys

# 분으로 변환
def convertToSec(hour, minute, sec):
    return hour * 60 * 60 + minute * 60 + sec

# string으로 변환
def convertToStr(num):
    hour, remain = divmod(num, 3600)
    minute, second = divmod(remain, 60)
    s_hour = '0' + str(hour) if hour < 10 else str(hour)
    s_minute = '0' + str(minute) if minute < 10 else str(minute)
    s_second = '0' + str(second) if second < 10 else str(second)
    return s_hour+':'+s_minute+':'+s_second

def solution(play_time, adv_time, logs):
    pl_hour, pl_min, pl_sec= list(map(int,play_time.split(':')))
    play_time = convertToSec(pl_hour, pl_min, pl_sec)
    adv_hour, adv_min, adv_sec = list(map(int,adv_time.split(':')))
    adv_time = convertToSec(adv_hour, adv_min, adv_sec)
    imos = [0 for _ in range(play_time+1)]
    for log in logs:
        start_time, end_time = log.split('-')
        st_hour, st_min, st_sec = list(map(int,start_time.split(':')))
        start_time = convertToSec(st_hour, st_min, st_sec)
        
        ed_hour, ed_min, ed_sec = list(map(int,end_time.split(':')))
        end_time = convertToSec(ed_hour, ed_min, ed_sec)
        
        #시작한 start_time에 +1
        #user가 2초에 시작했다면 imos[2]에 +1
        imos[start_time] += 1
        #종료된 end_time에 -1
        #user가 4초에 끝냈다면 4초에 시작했다는 것을 의미하는 imos[4]에 -1
        imos[end_time] -= 1

    #imos에 해당 구간에 몇명이 존재하는지 계산
    for i in range(1, len(imos)):
        imos[i] += imos[i-1]
    
    #imos[i]번째 까지 총 몇명이 있었는지 누적해서 계산
    for i in range(1, len(imos)):
        imos[i] += imos[i-1]

    max_val = -sys.maxsize
    max_time = 0
    #play time이 8초고 adv_time이 3초라면 0초 ~ 5초에 시작 가능
    #이에 play_time - adv_time(8-3) 까지 돌리기(5초까지 돌려야하므로 range(5+1)사용)
    for i in range(play_time-adv_time+1):
        if i != 0:
            val = imos[i+adv_time-1] - imos[i-1]
        else:
            #0초라면 빼야할 것이 없으므로 따로 else문에 설정
            val = imos[adv_time-1]
        if max_val < val:
            max_time = i
            max_val = val
    return convertToStr(max_time)
