def frequent(list):
    count = 0
    num = list[0]
    for i in list:
        current_count = list.count(i)
        if(current_count>count):
            count = current_count
            num=i
    print(num)

list = [1,1,2,2,2,3]
frequent(list)