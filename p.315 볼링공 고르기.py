n, m = map(int, input().split())
balls = list(map(int, input().split()))

balls_weight = [0] * (m+1)  # 공 무게별 개수 체크(0 ~ m까지)

for i in balls:
    balls_weight[i] += 1

total = 0

for i in range(1, m):
    total += balls_weight[i] * sum(balls_weight[i + 1:])

print(total)