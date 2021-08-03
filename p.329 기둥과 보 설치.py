def solution(n, build_frame):

    def base(n):
        res = []
        for i in range(n+1):
            temp = []
            for j in range(n+1):
                temp.append([j, i, 0, 0])
            res.append(temp)
        
        return res

    def check(block, x, y):
        res = True
        if block[y][x][2] == 1: # 기둥이면
            if y==0 or block[y-1][x][2]==1 or (x>0 and block[y][x-1][3]==1) or \
                block[y][x][3]==1:
                res = True
            else: return False
        
        if block[y][x][3] == 1: # 보이면
            if (y>0 and block[y-1][x][2]==1) or \
                (y>0 and x<n and block[y-1][x+1][2]==1) or \
                    (0<x<n and block[y][x-1][3]==1 and block[y][x+1][3]==1):
                res = True
            else: return False
        
        return res
                    
    block = base(n)

    for k in range(len(build_frame)):
        build = build_frame[k]
        x, y = build[0], build[1]
        type, act = build[2], build[3]

        if act == 1:
            if type == 0:
                block[y][x][2] += 1            
                if check(block, x, y) is False:
                    block[y][x][2] -= 1
            else:
                block[y][x][3] += 1
                if check(block, x, y) is False:
                    block[y][x][3] -= 1

        else:
            if type == 0:
                if block[y][x][2] > 0:
                    block[y][x][2] -= 1
                    if (check(block, x, y + 1) and \
                        check(block, x-1, y+1)) is False:
                        block[y][x][2] += 1
            else:
                if block[y][x][3] > 0:
                    block[y][x][3] -= 1
                    if (check(block, x, y) and check(block, x-1, y) and \
                        check(block, x+1, y)) is False:
                        block[y][x][3] += 1

    answer = []
    for i in range(len(block)):
        for j in range(len(block)):
            if block[j][i][2] > 0:
                answer.append([block[j][i][0], block[j][i][1], block[j][i][2]-1])
            if block[j][i][3] > 0:
                answer.append([block[j][i][0], block[j][i][1], block[j][i][3]])
    return answer                
    
