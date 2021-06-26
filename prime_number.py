def check_prime(n):
    factors = 0
    for i in range(2,n):
        if (n%i==0):
            factors+=1
    if factors>0:
        print("This number is not prime")
    else:
        print("This number is prime")

n = int(input("Enter a number: "))
if n==1 or n==2:
    print("The number is prime")
else:
    check_prime(n)
