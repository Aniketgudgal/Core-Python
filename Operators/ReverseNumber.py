''' Q21. Write a python program to reverse a number without using loop.
Input a number: 123 Reverse number: 321 ''' 

num = int(input("Enter the  3 digit number: "))

rev:int = 0
rem:int = 0
rem = num % 10
rev = rev* 10 + rem
num //= 10

rem = num % 10
rev = rev* 10 + rem
num //= 10

rem = num % 10
rev = rev* 10 + rem
num //= 10

print(type(rev))
print("Reverse number is: ",rev)