# Q12. Write a Python program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.

age = int(input("Enter the voter age: "))

if age >= 18:
	print("Voter is eligible to vote")
else:
	print("Not eligible")
