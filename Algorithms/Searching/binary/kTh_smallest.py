def Kth_smallest(arr, k, start, end):
    if start > end:
        for i in range(len(arr)):
            if arr[i] == start:
                return i
        return -1
    
    mid = (start + end) // 2
    count = 0
        
    for i in arr:
        if i <= mid:
            count += 1


    if count < k:
        return Kth_smallest(arr, k, mid + 1, end)
    
    else:
        return Kth_smallest(arr, k, start, mid - 1)
    

nums = [7, 10, 4, 3, 20, 15]
k = 5
idx = Kth_smallest(nums, k, 0, len(nums) - 1)
print(f"{k}th smallest element is {nums[idx]}")


    