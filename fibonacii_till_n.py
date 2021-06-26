n = int(input("Enter the limit of series: "))
sum = 1
a=0
b=1
print("Fibonacii series :")
while (sum<=n):
    print(sum)
    a = b
    b = sum
    sum = a+b
