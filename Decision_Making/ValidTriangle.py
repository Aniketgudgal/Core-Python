#Q2. Write a Python program to check whether a triangle is valid or not.

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

valid = side1 + side2 + side3
if valid == 180:
	print("Triagle is valid")
else:
	print("Triagle is not valid");