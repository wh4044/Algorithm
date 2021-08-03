from collections import deque
import copy

n = int(input())    # n 입력받기
indegree = [0] * (n + 1)    # 진입차수 리스트
time = [0] * (n + 1)    # 건설시간 저장할 리스트
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    # 값 입력 받아서 건설시간 저장
    data = list(map(int, input().split()))
    time[i] = data[0]

    for j in data[1:-1]:    # data의 맨 마지막인 -1을 제외하고 반복문
        indegree[i] += 1    # 먼저 지어져야할 건물 번호 진입차수 더해줌
        graph[j].append(i)

def topology_sort():
    result = copy.deepcopy(time)    # 결과과를 담을 result에 time을 복사
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0: q.append(i)    # 진입차수가 0이면 q에 추가

    while q:    # q가 빌 때까지 진행
        now = q.popleft()

        for i in graph[now]:
            # 기존 값과 새로운 값 중 더 큰 값으로 저장
            result[i] = max(result[i], time[i] + result[now])
            indegree[i] -= 1    # 진입차수 하나 빼기

            if indegree[i] == 0:    # 진입차수가 0이되면 q에 추가
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])    # 정답 출력

topology_sort()
