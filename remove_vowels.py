def remove_vowels(string):
	vowels = ("a","e","i","o","u")
	for x in string.lower():
		if x in vowels:
			string = string.replace(x,"")
	print(string)

string = str(input("Enter string: "))
remove_vowels(string)
