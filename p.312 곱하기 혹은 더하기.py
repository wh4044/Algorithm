s = input()

result = 0
for i in s:
    if int(i) <= 1 or result <= 1:
        result += int(i)
    else: result *= int(i)

print(result)