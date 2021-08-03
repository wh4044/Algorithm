# 2차원 리스트를 90도 회전한 결과를 반환하는 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for i in range(m)]    # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
            
    return result

def check(new_lock, n):
    for x in range(n, 2*n):
        for y in range(n, 2*n):
            if new_lock[x][y] != 1:
                return False
    return True


def solution(key, lock):
    n, m = len(lock), len(key)

    new_lock = [[0] * (3*n) for _ in range(3*n)]

    # 새 자물쇠의 가운데에 원래 자물쇠 집어넣기
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            new_lock[i][j] = lock[i-n][j-n]

    # 자물쇠에 키 끼워넣기
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for i in range(1, 2*n):
            for j in range(1, 2*n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                
                if check(new_lock, n): return True
                
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    
    return False

                