from collections import deque

n, m, k ,x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist_from_x = [-1] * (n + 1)
dist_from_x[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for i in graph[now]:
        if dist_from_x[i] == -1:
            dist_from_x[i] = dist_from_x[now] + 1
            q.append(i)

check = True
for i in range(1, len(dist_from_x)):
    if dist_from_x[i] == k:
        print(i)
        check = False

if check is True: print(-1)