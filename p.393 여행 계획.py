def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

INF = int(1e9)
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1): parent[i] = i

# graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    li = list(map(int, input().split()))
    for j in range(n):
        union_parent(parent, i, j+1)

nations = list(map(int, input().split()))

result = True
for i in range(m-1):
    root1 = find_parent(parent, nations[i])
    root2 = find_parent(parent, nations[i+1])

    if root1 != root2:
        result = False
        break

if result: print("YES")
else: print("NO")