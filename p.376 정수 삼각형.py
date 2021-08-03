n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(graph[i])):
        if j == 0: left_up = 0
        else: left_up = graph[i-1][j-1]

        if j == len(graph[i]) - 1: right_up = 0
        else: right_up = graph[i-1][j]

        graph[i][j] += max(left_up, right_up)

print(max(graph[-1]))