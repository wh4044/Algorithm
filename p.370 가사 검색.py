from bisect import bisect_left, bisect_right

def range_cnt(array, l, r):
    left = bisect_left(array, l)
    right = bisect_right(array, r)

    return right - left

def solution(words, queries):
    answer = []

    words_len = [[] for _ in range(10001)]
    words_len_rev = [[] for _ in range(10001)]

    for word in words:
        words_len[len(word)].append(word)
        words_len_rev[len(word)].append(word[::-1])

    for i in range(10001):
        words_len[i].sort()
        words_len_rev[i].sort()

    for q in queries:
        if q[0] != "?":
            cnt = range_cnt(words_len[len(q)], q.replace("?","a"), q.replace("?","z"))
        else:
            cnt = range_cnt(words_len_rev[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?","z"))
        
        answer.append(cnt)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
["fro??", "????o", "fr???", "fro???", "pro?"]))