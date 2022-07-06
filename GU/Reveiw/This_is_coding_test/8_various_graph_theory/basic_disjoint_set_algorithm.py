# 서로소 집합 알고리즘
node_num, edge_num = map(int, input().split())
parent = [i for i in range(node_num+1)]
print(parent)


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(node_1, node_2):
    parent_1 = find_parent(node_1)
    parent_2 = find_parent(node_2)
    if parent_1 > parent_2:
        parent[parent_1] = parent_2
    elif parent_2 > parent_1:
        parent[parent_2] = parent_1
    else:
        pass


for _ in range(edge_num):
    node_1, node_2 = map(int, input().split())
    union_parent(node_1, node_2)
    print(parent)

# 처음부터 끝까지 find_parent 해줘야 정상적으로 parent에 정상적인 값이 들어간다.
for i in range(1, node_num+1):
    find_parent(i)
print(*parent)
'''
# Remind
1. 서로소 집합 알고리즘:무방향 그래프에서 사이클 반별 가능 => 방향 그래프면 작은 수가 부모가 못되고 무조건 방향대로 설정되야해서 안됨.
                    dfs: 방향 그래프에서 사이클 판별 가능.
'''
