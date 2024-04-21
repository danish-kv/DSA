arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    val_min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[val_min]:
            val_min = j
    arr[i], arr[val_min] = arr[val_min], arr[i]

print(arr)


# Using Inbuild method min()

for i in range(len(arr)):
    min_val = min(arr[i:])
    min_index = arr.index(min_val, i)
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)
