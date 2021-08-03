n, k = map(int, input().split())    # n, k 입력받기

cnt = 0     # 횟수
while True:
    if n == 1: break  # n이 1이면 break
        
    if n % k == 0:  # n을 k로 나눌 수 있다면 나누고 횟수 + 1
        n /= k
        cnt += 1
    else:# n을 k로 나눌 수 없다면 n에 -1 하고 횟수 + 1
        n -= 1      
        cnt += 1

print(cnt)  # 결과 출력