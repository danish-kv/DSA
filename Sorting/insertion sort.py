arr = [100, 1, 20, 2, 90, 23, 1, 5, 67, 21]

for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > current:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = current
print(arr)



