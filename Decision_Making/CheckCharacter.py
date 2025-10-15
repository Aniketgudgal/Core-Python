#Q10. Write a Python program to input any character and check whether it is alphabet, digit or special character.

ch = input("Enter the Any Character input: ")[0]

if (ord(ch) >= 65 and ord(ch) <= 91) or (ord(ch) >= 97 and ord(ch) <= 122):
	print("The Input character is Alphabet")
elif ord(ch) >= 48 and ord(ch) <= 57:
	print("The Input character is Digit")
else:
	print("The input character is special")