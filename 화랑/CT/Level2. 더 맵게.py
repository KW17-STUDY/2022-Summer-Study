import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    heap = scoville
    while heap[0] < K:
        if len(heap)<=1:
            return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer += 1
    return answer