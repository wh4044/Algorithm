g = int(input())    # 탑승구의 수
p = int(input())    # 비행기의 수

gate = [True] * (g+1)
cnt = 0
dock = True

for i in range(p):
    num = int(input())
    for i in range(num, -1, -1):
        if i == 0:
            dock = False
            break

        if gate[i]:
            gate[i] = False
            cnt += 1
            break
    if not dock: break

print(cnt)