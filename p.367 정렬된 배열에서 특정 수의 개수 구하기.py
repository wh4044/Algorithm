from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
nums = list(map(int, input().split()))

def process(array, x):
    left = bisect_left(array, x)
    right = bisect_right(array, x)

    return right - left

print(process(nums, x) if process(nums, x) != 0 else -1)