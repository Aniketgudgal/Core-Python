#Q4. Write a Python program to check whether a number is positive , negative or zero.

num = int(input("Enter the number: "))
if num == 0:
	print("The number is Zero")
elif num > 0:
	print("The number is positive")
else:
	print("The number is negative")