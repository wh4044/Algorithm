n = int(input())

house = list(map(int, input().split()))
house.sort()

if n % 2 != 0: print(house[n//2])
else: print(house[n//2 - 1])