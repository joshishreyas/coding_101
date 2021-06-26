arr = [23,45,82,66,12,78,13,71,86]
max = 0
max_index = 0
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
        max_index = i
print(max)
print(max_index)
