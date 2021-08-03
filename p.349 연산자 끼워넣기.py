from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

li = ["+", "-", "*", "/"]
li_1 = list(map(int, input().split()))

li_2 = []
index = 0
for i in li_1:
    for j in range(i):
        li_2.append(li[index])
    index += 1

max_result = -1e9
min_result = 1e9

operator_combi = set(permutations(li_2, sum(li_1)))
for operator in operator_combi:
    index = 0
    result = nums[0]
    for i in range(1, len(nums)):
        if operator[index] == "+": result += nums[i]
        elif operator[index] == "-": result -= nums[i]
        elif operator[index] == "*": result *= nums[i]
        else: result = int(result / nums[i])
        index += 1
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)

# n = int(input())
# nums = list(map(int, input().split()))

# a, b, c, d = map(int, input().split())

# max_result = -1e9
# min_result = 1e9
# # DFS로 풀어보기
# def dfs(i, now):
#     global a,b,c,d,max_result,min_result

#     if i == n:
#         max_result = max(max_result, now)
#         min_result = min(min_result, now)

#     if a > 0:
#         a -= 1
#         dfs(i + 1, now + nums[i])
#         a += 1
    
#     if b > 0:
#         b -= 1
#         dfs(i + 1, now - nums[i])
#         b += 1
    
#     if c > 0:
#         c -= 1
#         dfs(i + 1, now * nums[i])
#         c += 1

#     if d > 0:
#         d -= 1
#         dfs(i + 1, int(now / nums[i]))
#         d += 1

# dfs(1, nums[0])

# print(max_result)
# print(min_result)