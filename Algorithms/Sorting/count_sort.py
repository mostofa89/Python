def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1, 1000]
    print("Array Before Counting Sort:", arr)
    sorted_arr = counting_sort(arr)
    print("Array After Counting Sort:", sorted_arr)


# time complexity: O(n + k) where n is the number of elements in input array and k is the range of input
# space complexity: O(k) where k is the range of input