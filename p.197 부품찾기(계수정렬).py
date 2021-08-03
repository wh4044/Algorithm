n = int(input())
array = [0] * 1000000

for i in input().split():
    array[int(i)] = 1

m = int(input())
li = list(map(int, input().split()))

for x in li:
    if array[x] == 1: print("yes", end = " ")
    else: print("no", end = " ")