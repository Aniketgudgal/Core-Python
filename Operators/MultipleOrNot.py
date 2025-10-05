''' Q30. Write a python program to check whether a number is a multiple of both 3 and 5 using logical AND (&&) operator.
Input: 15
Output: Multiple of both 3 and 5 '''

num = int(input("Enter the number: "))
if num % 3 == 0 and num % 5 == 0:
	print("The number is multiple of 3 and 5")
else:
	print("Not a multiple of 3 and 5")