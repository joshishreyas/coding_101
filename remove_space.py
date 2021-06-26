arr = [1,3,5,2,4]
n = len(arr)
print(arr)
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)