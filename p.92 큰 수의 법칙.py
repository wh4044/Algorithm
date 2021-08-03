N, M, K = map(int,input().split())

li = list(map(int, input().split()))
li.sort()

m1 = li.pop()
m2 = li.pop()

result = 0

# m1이 더해지는 횟수
cnt_m1 = (M // (K+1)) * K
cnt_m1 += M % (K+1)

# m1, m2 더하기

result += cnt_m1 * m1       # 가장 큰 수 더하기
result += (M-cnt_m1) * m2   # 두 번째로 큰 수 더하기

print(result)   # 결과 출력
