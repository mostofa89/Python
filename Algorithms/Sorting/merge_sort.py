def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        A = merge_sort(left_half)
        B = merge_sort(right_half)
        return merge(A, B)
    
    return nums


def merge(A, B):
    merged = []
    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    merged.extend(A[i:])
    merged.extend(B[j:])
    return merged


if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(sample_list)
    print("Sorted list is:", sorted_list)