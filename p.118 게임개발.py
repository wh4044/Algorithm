N, M = map(int, input().split())
A, B, d = map(int, input().split())

Map = []

for i in range(N):
    Map.append(list(map(int, input().split())))

while True:
    Map[A][B] = 9
    if Map[A-1][B] != 0 and Map[A+1][B] != 0 and Map[A][B-1] != 0 and Map[A][B+1] != 0:
        if d == 0 and Map[A + 1][B] != 1: 
            A += 1
            continue            
        elif d == 3 and Map[A][B+1] != 1: 
            B += 1
            continue
        elif d == 2 and Map[A-1][B] != 1: 
            A -= 1
            continue
        elif d == 1 and Map[A][B-1] != 1: 
            B -= 1
            continue
        break

    if d == 0:
        if Map[A][B-1] == 1 or Map[A][B-1] == 9: d = 3
        elif Map[A][B-1] == 0: 
            d = 3
            B -= 1
        continue

    if d == 3:
        if Map[A + 1][B] == 1 or Map[A + 1][B] == 9: d = 2
        elif Map[A + 1][B] == 0: 
            d = 2
            A += 1
        continue

    if d == 2:
        if Map[A][B+1] == 1 or Map[A][B+1] == 9: d = 1
        elif Map[A][B+1] == 0: 
            d = 1
            B += 1
        continue

    if d == 1:
        if Map[A-1][B] == 1 or Map[A-1][B] == 9: d = 0
        elif Map[A-1][B] == 0: 
            d = 0
            A -= 1
        continue

cnt = 0
for i in Map:
    for j in i:
        if j == 9:
            cnt += 1 
             
print(cnt)

'''
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for i in range(n)]

# 현재 캐릭터의 x,y 좌표와 방향 입력받기
x, y, direction = map(int,input().split()) 

d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수 생성
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
cnt = 1
turn_time = 0
while True:

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        cnt += 1
        turn_time = 0
        x = nx
        y = ny
        continue

    else: turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)
'''