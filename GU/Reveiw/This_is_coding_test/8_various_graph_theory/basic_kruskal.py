def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


node_num, edge_num = map(int, input().split())
parent = [i for i in range(node_num+1)]
edges = []

for _ in range(edge_num):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
print(edges)
total_cost = 0

for cost, a, b in edges:
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)
