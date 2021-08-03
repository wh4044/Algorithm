for _ in range(int(input())):
    n, m = map(int, input().split())

    li = list(map(int, input().split()))
    graph = []

    now = 0
    for i in range(m, n*m + 1, m):
        graph.append(li[now:i])
        now = i

    for j in range(1, m):
        for i in range(n):
            if i == 0: left_up = 0
            else: left_up = graph[i-1][j-1]

            if i == n-1: left_down = 0
            else: left_down = graph[i+1][j-1]

            left = graph[i][j-1]

            graph[i][j] += max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, graph[i][-1])

    print(result)