def sum(arr,n):
    if n == 1:
        return arr[0]
    else:
        return arr[n-1] + sum(arr,n-1)

arr = [1,2,3,4,5]
print(sum(arr,len(arr)))