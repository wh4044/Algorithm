def solution(s):
    word_len = 1e9

    if len(s) <= 1: return 1

    for i in range(1, len(s) // 2 + 1):
        words = []
        for j in range(0, len(s), i):
            word = s[j : j + i]
            words.append(word)

        cnt = 1
        string = ""
        for j in range(1, len(words)):
            if words[j] == words[j-1]: cnt += 1
            else:
                if cnt > 1: string += str(cnt) + words[j-1]
                else: string += words[j-1]
                cnt = 1

        if cnt > 1: string += str(cnt) + words[-1]
        else: string += words[-1]
        
        word_len = min(word_len, len(string))
    return word_len