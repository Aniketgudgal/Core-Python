''' Q26. Write a java program to Check Number Is Spy Number or Not.
Example :
A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits.
     Input : 1412
     Output : Spy Number 

Explanation :
sum = (1 + 4 + 1 + 2) = 8
product = (1 * 4 * 1 * 2) = 8
since, sum == product == 8 '''

num = int(input("Enter the 4 digit number: "))

sum =0
product = 1
rem = 0

rem = num % 10
sum += rem
product *= rem
num //= 10

rem = num % 10
sum += rem
product *= rem
num //= 10

rem = num % 10
sum += rem
product *= rem
num //= 10

rem = num % 10
sum += rem
product *= rem
num //= 10

if sum == product:
	print("The number is Spy")
else:
	print("Not a Spy number")