def first_one(nums, key, start, end, first_idx):
    if start > end:
        return first_idx
    mid = (start + end) // 2

    if nums[mid] == key:
        first_idx = mid
        return first_one(nums, key, start, mid - 1, first_idx)
    
    elif nums[mid] < key:
        return first_one(nums, key, mid + 1, end, first_idx)
    
    else:
        return first_one(nums, key, start, mid - 1, first_idx)
    


# nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
nums = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8]
key = 2

print(f"First index of {key} is {first_one(nums, key, 0, len(nums) - 1, first_idx = -1)}")
    