def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        if min_idx != i:
            temp = nums[i]
            nums[i] = nums[min_idx]
            nums[min_idx] = temp

    return nums


if __name__ == "__main__":
    sample_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(sample_list)
    print("Sorted list is:", sorted_list)