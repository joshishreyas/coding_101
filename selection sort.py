arr = [4,2,1,3,5]
for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
        if arr[min]>arr[j]:
            min=j
    arr[min],arr[i]=arr[i],arr[min]
print(arr)
