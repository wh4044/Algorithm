n, m = map(int, input().split())

mins = 0

for i in range(n):
    line = list(map(int, input().split()))
    mins = max(mins, min(line))

print(mins)