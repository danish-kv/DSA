def pivot_index(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]

    return right


def quicksort(arr, first, last):
    if first < last:
        p = pivot_index(arr, first, last)
        quicksort(arr, first, p - 1)
        quicksort(arr, p + 1, last)


array = [64, 34, 25, 12, 22, 11, 90]
print(array)
quicksort(array, 0, len(array) - 1)
print(array)