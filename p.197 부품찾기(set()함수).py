n = int(input())

array = set(map(int, input().split()))

m = int(input())
li = list(map(int, input().split()))

for x in li:
    if x in array: print("yes", end = " ")
    else: print("no", end = " ")