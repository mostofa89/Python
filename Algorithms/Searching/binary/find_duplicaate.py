def find_duplicate(nums, start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    count = 0
    for num in nums:
        if start <= num <= mid:
            count += 1

    if count > (mid - start + 1):
        return find_duplicate(nums, start, mid)
    
    else:
        return find_duplicate(nums, mid + 1, end)
    

nums = [3, 1, 4, 4, 2]
n = len(nums) - 1
duplicate = find_duplicate(nums, 1, n)
print(f"The duplicate number is: {duplicate}")  # Output: The duplicate number is: 4
