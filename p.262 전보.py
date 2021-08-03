import heapq
import sys

input = sys.stdin.readline

n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

start = c

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

cnt = 0
dist_max = 0
for i in distance:
    if i != INF:
        cnt += 1
        dist_max = max(dist_max, i)

print(cnt-1, dist_max)