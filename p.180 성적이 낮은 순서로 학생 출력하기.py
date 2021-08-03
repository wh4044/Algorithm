n = int(input())

array = []

for i in range(n):
    (name, score) = input().split()
    array.append((name, int(score)))

def setting(data):
    return data[1]

array = sorted(array, key = lambda data : data[1])

for i in array:
    print(i[0], end = " ")