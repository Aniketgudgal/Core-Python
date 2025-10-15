#Q6. Write a Python program to check whether a character is alphabetic or not.

num = input("Enter character: ")
if (ord(num[0]) >= 65 and ord(num[0]) <= 91) or ord(num[0]) >= 97 and ord(num[0]) <= 122: # character convert into ASCII value using ord function and check with ASCII number
	print("The Give input Alphabet")
else:
	print("Not a Alphabet")