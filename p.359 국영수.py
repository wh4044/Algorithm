n = int(input())

info = [list(input().split()) for _ in range(n)]

info.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in info: print(i[0])