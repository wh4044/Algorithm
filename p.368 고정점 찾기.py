n = int(input())
nums = list(map(int, input().split()))

def binary(array, start, end):
    if start > end: return None
    mid = (start + end) // 2
    if array[mid] == mid: return mid

    elif mid > array[mid]:
        return binary(array, mid + 1, end)

    elif mid < array[mid]:
        return binary(array, start, mid - 1)
    

result = binary(nums, 0, n-1)
if result == None: print(-1)
else: print(result)