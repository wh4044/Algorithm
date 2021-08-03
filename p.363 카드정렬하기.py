import heapq

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

total = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    summary = a + b
    total += summary

    heapq.heappush(heap, summary)

print(total)