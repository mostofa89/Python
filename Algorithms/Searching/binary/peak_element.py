def find_peak_index(arr, left, right):
    if left == right:
        return left

    mid = (left + right) // 2

    if arr[mid] < arr[mid + 1]:
        return find_peak_index(arr, mid + 1, right)
    
    return find_peak_index(arr, left, mid)


nums = [1, 2, 1, 3, 5, 6, 4, 7]
idx = find_peak_index(nums, 0, len(nums) - 1)
print(f"Peak element is {nums[idx]} at index {idx}")
