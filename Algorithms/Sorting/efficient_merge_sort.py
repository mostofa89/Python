def merge_sort(nums):
    temp = [0] * len(nums)
    _merge_sort(nums, 0, len(nums) - 1, temp)
    return nums


def _merge_sort(nums, left, right, temp):
    if left >= right:
        return

    mid = (left + right) // 2

    _merge_sort(nums, left, mid, temp)
    _merge_sort(nums, mid + 1, right, temp)
    merge(nums, left, mid, right, temp)


def merge(nums, left, mid, right, temp):
    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = nums[j]
        j += 1
        k += 1

    for k in range(left, right + 1):
        nums[k] = temp[k]


if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(sample_list)
    print("Sorted list is:", sorted_list)