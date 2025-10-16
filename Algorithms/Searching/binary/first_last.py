def find_FirstIdx(nums, target, start, end, firstIdx):
    if start > end:
        return firstIdx
    
    mid = (start + end) // 2
    if nums[mid] == target:
        firstIdx = mid
        return find_FirstIdx(nums, target, start, mid - 1, firstIdx)
    
    elif nums[mid] > target:
        return find_FirstIdx(nums, target, start, mid - 1, firstIdx)
    
    else:
        return find_FirstIdx(nums, target, mid + 1, end, firstIdx)
    

def find_LastIdx(nums, target, start, end, lastIdx):
    if start > end:
        return lastIdx
    
    mid = (start + end) // 2
    if nums[mid] == target:
        lastIdx= mid
        return find_LastIdx(nums, target, mid + 1, end, lastIdx)
    
    elif nums[mid] > target:
        return find_LastIdx(nums, target, start, mid - 1, lastIdx)
    
    else:
        return find_LastIdx(nums, target, mid + 1, end, lastIdx)


nums = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8]
key = 7
print(f"First index of {key} is {find_FirstIdx(nums, key, 0, len(nums) - 1, -1)} and last of {key} is {find_LastIdx(nums, key, 0, len(nums) - 1, -1)}.")

