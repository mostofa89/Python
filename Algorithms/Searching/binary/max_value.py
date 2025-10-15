#finding minium value using in rotate array using binary search
def max_value(nums, start, end):
    mid = (start + end) // 2

    if len(nums) == 0:
        return -1
    
    if len(nums) == 1:
        return nums[0]

    if start == end:
        return nums[mid - 1]

    elif nums[mid] > nums[end]:
        return max_value(nums, start + 1, end)
    
    else:
        return max_value(nums, start, mid)
    

if __name__ == "__main__":
    nums = [10, 12, 14, 16, 6, 6, 8, 9]
    # nums = [2]
    print(f"Maxinum value is {max_value(nums, 0, len(nums) - 1)}.")