''' Q24. Write a java program to check whether number is neon or not.
Input : 9
Output : Neon Number Explanation: square is 9*9 = 81 and sum of the digits of the square is 9. '''

num = int(input("Enter the number: "))
temp = num
sq = num*num;
sum = 0
sum += sq%10
sq //= 10

sum+= sq%10

if temp == sum:
	print("Number is Neon")
else:
	print("Number is not Neon")