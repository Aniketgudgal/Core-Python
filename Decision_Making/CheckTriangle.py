#Q3. Write a python program to check whether a triangle is equilateral , isoscale  or scalene.

side1: int = input("Enter the first side: ")
side2: int = input("Enter the second side: ")
side3: int = input("Enter the third side: ")

if side1 == side2 and side1 == side3:
	print("The triangle is equilateral")
elif side1 == side2 or side3 == side2 or side1 == side3:
	print("the triangle is isoscale")
else:
	print("The triangle is scalene")