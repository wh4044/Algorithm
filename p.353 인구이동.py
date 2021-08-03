from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def move(index, x, y):
    union_list = []
    q = deque()
    q.append((x, y))
    union_list.append((x, y))
    total = graph[x][y]
    union[x][y] = index
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                dif = abs(graph[nx][ny] - graph[x][y])
                if l <= dif <= r:
                    union_list.append((nx, ny))
                    q.append((nx, ny))
                    total += graph[nx][ny]
                    union[nx][ny] = index
                    
    for x, y in union_list:
        graph[x][y] = total // len(union_list)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

move_cnt = 0
while True:
    union = [[-1]  * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                move(index,i,j)
                index += 1
            
    if index == n * n: break

    move_cnt += 1

print(move_cnt)