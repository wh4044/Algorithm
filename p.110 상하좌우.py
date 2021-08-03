n = int(input())

x, y = 1, 1

move = list(input().split())

for i in move:
    if i == "R" and y + 1 <= n:
        y += 1
    elif i == "L" and y - 1 >= 1:
        y -= 1
    elif i == "U" and x - 1 >= 1:
        x -= 1
    elif i == "D" and x + 1 <= n:
        x += 1

print(x, y)