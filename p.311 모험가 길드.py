n = int(input())
group = list(map(int, input().split()))

group.sort()
cnt = 0
result = 0
for i in group:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)