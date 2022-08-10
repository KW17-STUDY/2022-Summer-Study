from collections import defaultdict

# 효율성 테스트 불통
def solution(food_times, k):
    answer = 0
    foods = defaultdict(int)
    order= []
    for idx, food in enumerate(food_times):
        foods[idx] = food
    while True:
        for i in foods:
            if foods[i] >0:
                order.append(i)
                foods[i]-=1
        if sum(foods.values()) == 0:
            break
    if k>len(order)-1:
        answer = -1
    else:
        answer = order[k]+1
    return answer

# solution
# 무지의 먹방 라이브
import heapq


def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time
    print(h)
    print(h[1][0])
    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            # heapq로 인해 바뀌었던 순서를 원래 음식의 번호대로 다시 sorting하기
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer
'''
#Remind
1. heapq을 사용해서 문제 해결
걸리는 시간을 기준으로 오름차순으로 정렬한 이후, (앞 뒤 시간 간격)*전체 남은 음식 개수를 해서
pop해서 꺼낸 음식을 다 먹을 수 있는지 검사 한다.
만약 먹을 수 없다면, 바퀴수를 돌릴 수 있을 때 까지 돌려 나온 나머지(k%food_num)을 구해서
다음에 먹어야할 음식을 구한다.
2. 이전 음식과 지금 음식(방금 pop한 음식)의 시간이 같을 경우 0*food_time이 되므로 잘 돌아간다.
3. 원의 형태로 차례대로 순회하여 중단되서 어디서부터 수행해야할지 구하는 문제는 이처럼 heapq를 이용하여
적게 걸리는 음식을 기준으로 몇 초가 걸려야 다 먹을 수 있는지 계산한다. 이후 이 값을 전체 시간에서 뺴주어
음수가 된다면 돌릴 수 있는 바퀴수를 전부 돌리고 나머지를 구하여 답을 구하고(k % food_num)
양수가 된다면 전체 시간에서 제일 적게 걸리는 음식((h[0][0] - previous) * food_num)을 몇초만에 다먹을 수 있는지
구했던 값을 빼고 위의 과정(제일 적게 걸리는 음식을 몇초만에 먹을 수 있는지 구하기) 계속 진행한다.
'''