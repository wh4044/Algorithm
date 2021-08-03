s = input()


# 1 묶음 개수
cnt_1 = 0
# 0 묶음 개수
cnt_0 = 0
if s[0] == "0": cnt_0 += 1
else: cnt_1 += 1

for i in range(1, len(s)):
    if s[i-1] == "0" and s[i] == "1":
        cnt_1 += 1

    elif s[i-1] == "1" and s[i] == "0":
        cnt_0 += 1

print(min(cnt_0, cnt_1))


s = input()    # 문자열을 받음

cnt_1 = 0    # 1 묶음 개수
cnt_0 = 0    # 0 묶음 개수

# s의 첫 문자가 0, 1 여부에 따라서 각 묶음 개수에 +1을 해준다.
if s[0] == "0": cnt_0 += 1
else: cnt_1 += 1

# i번 인덱스와 i-1번 인덱스를 비교하여 어떤 묶음의 개수를 증가시킬지 판단
for i in range(1, len(s)):
    # 0에서 1로 바뀌는 경우 1 묶음의 개수를 증가시킴
    if s[i-1] == "0" and s[i] == "1":
        cnt_1 += 1

    # 1에서 0으로 바뀌는 경우 0 묶음의 개수를 증가시킴
    elif s[i-1] == "1" and s[i] == "0":
        cnt_0 += 1

    # 0에서 0으로 또는 1에서 1로 바뀌는 경우는 무시

print(min(cnt_0, cnt_1))    # 결과적으로 0, 1 묶음 중에서 작은 값을 출력