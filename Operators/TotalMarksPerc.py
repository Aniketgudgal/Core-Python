''' Q11. Write a python program to enter marks of five subjects and calculate total marks and percentage. '''

mark1 = int(input("Enter the marks of 1st subject: "))
mark2 = int(input("Enter the marks of 2nd subject: "))
mark3 = int(input("Enter the marks of 3rd subject: "))
mark4 = int(input("Enter the marks of 4th subject: "))

totalMark = mark1 + mark2 + mark3 + mark4
print("The total marks is: ",totalMark)

percentage = (totalMark / 400)*100

print("percentage is: ",percentage)