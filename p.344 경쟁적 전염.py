from copy import *
from collections import deque

# # 상하좌우 바이러스 퍼뜨리기
# def virus(v, x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = v

n, k = map(int, input().split())

graph = []
q = []

for i in range(n):
    li = list(map(int, input().split()))
    graph.append(li)
    for j in range(n):
        if li[j] != 0:
            q.append((li[j], i, j, 0))
q.sort()
q = deque(q)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    v, a, b, time = q.popleft()

    if time == s: break

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append((v, nx, ny, time + 1))

print(graph[x-1][y-1])