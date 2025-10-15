#finding minium value using in rotate array using binary search
def find_min(nums, start, end):
    mid = (start + end) // 2
    if start == end:
        return nums[start]

    if nums[mid] > nums[end]:
        return find_min(nums, start + 1, end)
    
    else:
        return find_min(nums, start, mid)
    

if __name__ == "__main__":
    # nums = [10, 12, 14, 16, 6, 6, 8, 9]
    nums = [2, 3, 4, 1]
    print(f"Mininum value is {find_min(nums, 0, len(nums) - 1)}.")