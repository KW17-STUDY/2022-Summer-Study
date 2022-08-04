import sys
from collections import defaultdict

max_sheep = -sys.maxsize
is_worf = []
def makeInputList(edges):
    input_list = defaultdict(list)
    for e_v, s_v in edges:
        input_list[e_v].append(s_v)
    return input_list

def recursive(cur_node, num_worf, num_sheep, enable, visited):
    global is_worf, list_edges, max_sheep
    
    # 현재 노드가 늑대인지 아닌지 본 후, 마리 수 추가
    if is_worf[cur_node]:
        num_worf+=1
    else:
        num_sheep += 1
        max_sheep = max(max_sheep, num_sheep)
                    
    #늑대의 마리수가 양 이상이라면 종료                    
    if num_worf >= num_sheep:
        return
    
    #현재 노드 방문 처리
    visited[cur_node] = True
    
    #현재 노드와 연결되어 있는 노드를 enable에 추가
    for i in list_edges[cur_node]:
        enable.append(i)
        
    
    for next_node in enable:
        recursive(next_node, num_worf, num_sheep, \
            # 현재 노드를 enable에서 없애기 위해 and not visted[i] 사용
            # 다음 방문할 노드 또한 enable에서 제외
            # visited는 포인터기 때문에 visited[:]로 값 자체를 대입
            [i for i in enable if i!=next_node and not visited[i]], visited[:])
    
def solution(info, edges):
    global is_worf, list_edges

    visited = [False for _ in range(len(info))]
    is_worf = info
    num_worf, num_sheep = 0, 0
    list_edges = makeInputList(edges)
    recursive(0, num_worf, num_sheep, [], visited)
    return max_sheep

'''
import sys
from collections import defaultdict

max_sheep = -sys.maxsize
is_worf = []
def makeInputList(edges):
    input_list = defaultdict(list)
    for e_v, s_v in edges:
        input_list[e_v].append(s_v)
    return input_list

def recursive(cur_node, num_worf, num_sheep, enable):
    global is_worf, list_edges, max_sheep
    
    # 현재 노드가 늑대인지 아닌지 본 후, 마리 수 추가
    if is_worf[cur_node]:
        num_worf+=1
    else:
        num_sheep += 1
        max_sheep = max(max_sheep, num_sheep)
                    
    #늑대의 마리수가 양 이상이라면 종료                    
    if num_worf >= num_sheep:
        return
    
    #현재 노드 방문 처리
    
    #현재 노드와 연결되어 있는 노드를 enable에 추가
    for i in list_edges[cur_node]:
        enable.append(i)
        
    
    for next_node in enable:
        recursive(next_node, num_worf, num_sheep, \
            # 현재 노드를 enable에서 제거
            # 다음 방문할 노드 또한 enable에서 제외
            [i for i in enable if i!=next_node and i!=cur_node])
    
def solution(info, edges):
    global is_worf, list_edges
    is_worf = info
    num_worf, num_sheep = 0, 0
    enable = []
    list_edges = makeInputList(edges)
    recursive(0, num_worf, num_sheep, [])
    return max_sheep
'''

'''
# Remind
1. 처음보는 문제였다. dfs, bfs문제가 아니라고 생각해서 당황했는데 생각을 구현을 못한 문제이다.
list에 다음으로 이동할 수 있는 노드를 추가시키고 현재노드와 다음 들어갈 노드를 이동할 수 있는 노드를 저장하고 있는
enable list에서 빼주어 구현하면 쉽게 풀 수 있다.
핵심은 [i for i in enable if i!=next_node and i!=cur_node]) 이다.
[i for i in enable if i!=next_node and not visited[i]], visited[:]]로도 풀 수 있다.
visited를 통해 현재 노드를 걸러줄 것인지 아니면 그냥 명시적으로 걸러줄 것인지의 차이이다.
'''