def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


node_num, edge_num = map(int, input().split())
parent = [i for i in range(node_num+1)]
cycle = False
for _ in range(edge_num):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        print('cycle 오류')
        print(*parent)
        cycle = True
        break
    else:
        union_parent(parent, a, b)
        print(*parent)

if cycle:
    print('cycle이 발생했습니다.')
else:
    print('cycle이 발생하지 않았습니다.')
