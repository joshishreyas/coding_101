list = [4,2,3,1,5]
for i in range(1,len(list)):
    key = list[i]
    j=i-1
    while j>=0 and key<list[j]:
        list[j+1]=list[j]
        j-=1
    list[j+1]=key
print(list)
