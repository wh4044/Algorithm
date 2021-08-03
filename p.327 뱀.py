from collections import deque

n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수

graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 2

l = int(input())    # 방향 변환 횟수
second, points = deque(), deque()
for i in range(l):
    sec, point = input().split()
    second.append(sec)
    points.append(point)

def turn(point):
    global d
    if point == "D":
        d += 1
        if d == 4: d = 0
    else:
        d -= 1
        if d == -1: d = 3

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


time_cnt = 0
d = 0

q = deque()
x, y = 1, 1
graph[x][y] = 1
q.append((x,y))
while True:
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 1 or nx > n or ny < 1 or ny > n or graph[nx][ny] == 1:
        time_cnt += 1
        break

    if graph[nx][ny] == 2:
        q.append((nx, ny))
        graph[nx][ny] = 1
        time_cnt += 1
    
    elif graph[nx][ny] == 0:
        graph[nx][ny] = 1
        qx, qy = q.popleft()
        graph[qx][qy] = 0
        q.append((nx,ny))
        time_cnt += 1

    if second and time_cnt == int(second[0]):
        second.popleft()
        p = points.popleft()
        turn(p)
    

    x, y = nx, ny

print(time_cnt)
    