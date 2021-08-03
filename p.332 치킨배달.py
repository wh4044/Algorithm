from itertools import combinations

n, m = map(int,input().split())

chicken_spot, house = [], []

for i in range(n):
    spot = list(map(int ,input().split()))
    for j in range(len(spot)):
        if spot[j] == 1: house.append((i,j))
        if spot[j] == 2: chicken_spot.append((i,j))

chicken_pick = list(combinations(chicken_spot, m))

min_dist_sum = 1e9
for chic in chicken_pick:
    dist_sum = 0

    for hx, hy in house:
        min_dist = 1e9
        for cx, cy in chic:
            dist = abs(cx-hx) + abs(cy-hy)
            min_dist = min(min_dist, dist)
        dist_sum += min_dist
    
    min_dist_sum = min(min_dist_sum, dist_sum)

print(min_dist_sum)