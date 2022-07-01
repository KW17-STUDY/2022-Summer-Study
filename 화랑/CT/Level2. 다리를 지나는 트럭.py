from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    bridge = deque(0 for i in range(bridge_length))
    bridge_weigth = 0
    while 1:
        if len(truck)==0 and sum(bridge)==0:
            break
        if len(truck)!=0:
            if bridge_weigth-bridge[0]+truck[0] <= weight:
                temp = truck.popleft()
                bridge_weigth -= bridge[0]
                bridge.popleft()
                bridge.append(temp)
                bridge_weigth += temp
            else:
                bridge_weigth -= bridge[0]
                bridge.popleft()
                bridge.append(0)
        else:
            bridge_weigth -= bridge[0]
            bridge.popleft()
            bridge.append(0)
        answer += 1
    return answer