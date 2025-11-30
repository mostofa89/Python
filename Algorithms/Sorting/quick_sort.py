def quickSort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
    return arr


def partition(arr, low, high):
  pivot = arr[high]       # Correct pivot position for Lomuto
  i = low - 1

  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      swap(arr, i, j)

  swap(arr, i + 1, high)  # Place pivot in the correct position
  return i + 1


def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]



if __name__ == "__main__":
    arr = [35, 30, 28, 22, 34, 35, 26]
    print("Array Before Quick sort :", arr)
    print("Array After Quick sort :", quickSort(arr, 0, len(arr) - 1))
