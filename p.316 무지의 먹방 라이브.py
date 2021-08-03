import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    food = []
    for i in range(len(food_times)):
        heapq.heappush(food, (food_times[i], i+1))
    
    length = len(food_times)
    time_use = 0
    time_previous = 0

    while time_use + (food[0][0] - time_previous) * length <= k:
        now = heapq.heappop(food)[0]
        time_use += (now - time_previous) * length
        length -= 1
        time_previous = now

    food.sort(key = lambda x : x[1])
    return food[(k-time_use) % length][1]