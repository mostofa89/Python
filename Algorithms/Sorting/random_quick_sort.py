import random

def quickSort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr

def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    swap(arr, pivot_index, high)
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr = [35, 30, 28, 22, 34, 35, 26]
    print("Array Before Quick Sort:", arr)
    quickSort(arr, 0, len(arr) - 1)
    print("Array After Quick Sort: ", arr)
