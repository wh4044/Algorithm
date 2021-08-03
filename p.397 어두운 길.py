def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

n, m = map(int, input().split())
parent = [0] * n
for i in range(n): parent[i] = i
edges = []
cost_sum = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    cost_sum += c
    edges.append((c, a, b))

edges.sort()
result  = 0
for i in edges:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(cost_sum - result)