n = int(input())
day, pay = [], []
for _ in range(n):
    d, p = map(int, input().split())
    day.append(d)
    pay.append(p)

dp = [0] * (n + 1)
max_pay = 0

for i in range(n - 1, -1, -1):
    if day[i] + i <= n:
        dp[i] = max(pay[i] + dp[day[i] + i], max_pay)
        max_pay = dp[i]
    
    else: dp[i] = max_pay
    
print(max_pay)