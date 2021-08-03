from copy import *
import sys
from itertools import combinations

# 바이러스를 퍼뜨리는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: cnt += 1
    return cnt

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
empty_space = []

for i in range(n):
    li = list(map(int, input().split()))
    graph.append(li)
    for j in range(m):
        if li[j] == 0: empty_space.append((i,j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

wall_combi = list(combinations(empty_space, 3))



max_safety_zone = 0
for walls in wall_combi:
    for wx, wy in walls:
        graph[wx][wy] = 1
    
    temp = deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2: virus(i,j)
    
    safety_zone = check()

    max_safety_zone = max(max_safety_zone, safety_zone)

    for wx, wy in walls:
        graph[wx][wy] = 0

    
print(max_safety_zone)