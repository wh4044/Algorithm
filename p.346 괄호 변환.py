def check(a):
    if a[0] == "(": return True # 올바른 괄호 문장
    return False    # 균형잡힌 괄호 문장

def solution(p):
    string = ""
    if p == "": return string

    cnt_o, cnt_c = 0, 0
    for i in p:
        if i == "(": cnt_o += 1
        else: cnt_c += 1

        if cnt_o == cnt_c: break
    
    u = p[: cnt_o + cnt_c]
    v = p[cnt_o + cnt_c :]

    if check(u): 
        string = u + solution(v)
    
    else:
        string = "("
        string += solution(v)
        string += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(": u[i] = ")"
            else: u[i] = "("
        for i in u:
            string += i
        
    return string