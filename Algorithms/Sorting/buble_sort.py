def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swap = False
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                swap = True

        if not swap:
            print("Array is sorted. Exiting early.")
            return nums
        

    return nums


if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 6, 4, 2, 0]
    sorted_list = bubble_sort(sample_list)
    print("Sorted list is:", sorted_list)