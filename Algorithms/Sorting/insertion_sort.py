def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key


if __name__ == "__main__":
    sample_list = [12, 11, 13, 5, 6]
    insertion_sort(sample_list)
    print("Sorted list is:", sample_list)