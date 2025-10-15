def binary_search(nums, key, start, end):
    mid = (start + end) // 2
    if start >= end:
        return -1
    
    if nums[mid] == key:
        return mid
    
    if nums[mid] > key:
        return binary_search(nums, key, start, mid -1)
    
    else:
        return binary_search(nums, key, mid + 1, end)
    


nums = [2, 3, 4, 6, 7, 10, 12, 15, 18, 19, 20]
key = 20
print(f"The value index of {key} is {binary_search(nums, key, 0, len(nums))}.")
