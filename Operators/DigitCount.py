''' Q20. Write a Python program and compute the sum of an integer's digits.
Input : 123
Output : 6 '''

num = int(input("Enter 3 digit number: "))
sum = 0
sum += num % 10
num /= 10
sum += num % 10
num /= 10
sum += num % 10
print("The sum of all is: ",int(sum)) # type Casting fload to int