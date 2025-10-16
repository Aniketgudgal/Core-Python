# Q11. Write a Python program to find a maximum between three numbers.

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

if a > b and a > c:
	print("First value is maximum")
elif b > a and b > c:
	print("Second value is maximum")
else:
	print("Third value is maximum")