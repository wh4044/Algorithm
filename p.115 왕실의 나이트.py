spot = input()
# a ~ h : 97 ~ 104
cnt = 0

n1 = [1,2]
n2 = [-1,2]
n3 = [1,-2]
n4 = [-1,-2]

m1 = [2,1]
m2 = [2,-1]
m3 = [-2,1]
m4 = [-2,-1]

move_list = [n1,n2,n3,n4,m1,m2,m3,m4]


for move in move_list:
    y = ord(f"{spot[0]}")
    x = int(spot[1])

    x += move[0]
    y += move[1]

    if 97 <= y <= 104 and 1 <= x <= 8:
        cnt += 1

print(cnt)
