def solution(n, stages):
    total = len(stages)
    li = []
    for lv in range(1, n+1):
        cnt = stages.count(lv)
        if cnt == 0: fail = 0
        else: fail = cnt / total

        li.append((lv, fail))
        total -= cnt

        
    li.sort(key = lambda x : (-x[1], x[0]))

    nums = [i[0] for i in li]
    return nums