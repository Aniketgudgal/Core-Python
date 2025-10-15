#Q5. Write a Python program to check whether a number is divisible by 5 and 11 or not.

num = int(input("Enter the number: "))

if num % 5 == 0 and num % 11 == 0:
	print("The number is divisible by 5 and 11")
else:
	print("Not divisible by 5 and 11")