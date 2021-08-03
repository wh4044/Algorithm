from itertools import combinations

n = int(input())
graph, teachers, blanks = [], [], []

for i in range(n):
    maps = list(input().split())
    graph.append(maps)
    for j in range(n):
        if maps[j] == "T": teachers.append((i, j))
        if maps[j] == "X": blanks.append((i, j))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# 선생님의 시야에 학생이 있는지 판단하는 함수
def find(d, x, y):
    if d == 0:
        while x >= 0:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            x -= 1
    
    elif d == 1:
        while y < n:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            y += 1
    
    elif d == 2:
        while x < n:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            x += 1
    
    elif d == 3:
        while y >= 0:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            y -= 1
    
    return False

blank = list(combinations(blanks, 3))

# 학생 있는지 확인하는 함수
def check():
    for tx, ty in teachers:
        for i in range(4):
            if find(i, tx, ty): # 학생을 찾으면
                return True    
    return False

finding = False # 학생 아직 못찾았다고 초기화

for walls in blank:
    for wx, wy in walls:
        graph[wx][wy] = "O"
    
    if not check():
        finding = True
        break

    for wx, wy in walls:
        graph[wx][wy] = "X"

if finding: print("YES")
else: print("NO")