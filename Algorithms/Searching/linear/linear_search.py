def linear_search(nums, key):
    for i in range(len(nums)):
        if nums[i] == key:
            return i
        

    return -1



nums = [1, 2, 5, 7, 8, 10, 4, 3, 101, 100]
key = 15
print(f"The value index of {key} is {linear_search(nums, key)}.")