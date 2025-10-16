#Q16. Write a Python program to find a minimum between three numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < b and a < c:
	print("First number is minimum")
elif b < a and b < c:
	print("Second number is minimum")
else:
	print("Third number is minimum")