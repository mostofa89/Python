def search_Insertion(arr, target, start, end):
    if start > end:
        return start
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return search_Insertion(arr, target, mid + 1, end)
    
    else:
        return search_Insertion(arr, target, start, mid - 1)
    


nums = [1, 3, 5, 6]
idx = search_Insertion(nums, 8, 0, len(nums) - 1)
print(f"Target can be inserted at index {idx}")
