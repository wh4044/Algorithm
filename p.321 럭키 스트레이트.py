num = input()

half_index = len(num) // 2

left, right = 0, 0
for i in range(len(num)):
    if i < half_index: left += int(num[i])
    else: right += int(num[i])

print("LUCKY" if left == right else "READY")