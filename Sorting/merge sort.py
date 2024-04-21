def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
                k += 1
            else:
                arr[k] = right_half[j]
                j += 1
                k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


array = [12, 2333, 4, 0, 111, 212, 54]

print('Unsorted:-', array)
mergesort(array)
print('Sorted:-', array)
