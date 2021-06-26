def remove_duplicates(string):
	newstring = ""
	for x in string:
		if x not in newstring:
			newstring = newstring + x
	print(newstring)

string = str(input("Enter a string: "))
remove_duplicates(string)