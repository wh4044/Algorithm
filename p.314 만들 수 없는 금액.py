n = int(input())

moneys = list(map(int, input().split()))
moneys.sort()

total = 1
if min(moneys) >= 2: print(1)
else:
    for i in moneys:
        if i > total:
            break
        total += i

print(total)