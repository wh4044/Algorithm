def solution(s):
	word_len = 1e9
    
	if len(s) <= 1:
		word_len = min(word_len, len(s))
		return word_len
    
	for i in range(1, len(s) // 2 + 1):
		words = []
        
		for j in range(0,len(s), i):
			word = s[j:j+i]
			words.append(word)	
            
		result = ""
		cnt = 1
		for i in range(1, len(words)):
			if words[i] == words[i-1]: cnt += 1
			elif words[i] != words[i-1]:
				if cnt == 1:
					cnt = ""
				result += str(cnt) + words[i-1]
				cnt = 1		
                
			if i == len(words) - 1:
				if cnt == 1:
					cnt = ""
				result += str(cnt) + words[i]	
                
		word_len = min(word_len, len(result))	
	return word_len