def find_gcd(x, y):
	while(y):
		x, y = y, x % y

	return x
	
list = [3, 4, 6, 8, 16]

num1 = list[0]
num2 = list[1]
gcd = find_gcd(num1,num2)

for i in range(2,len(list)):
	gcd = find_gcd(gcd,list[i])
	
print(gcd)

