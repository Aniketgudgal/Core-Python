''' Q28. Write a python program to calculate the net salary of an employee.
Input: basic salary, HRA %, DA %, and tax %. '''

salary = int(input("Enter the salary of employee: "))
hra = int(input("Enter hra is percentage: "))
da = int(input("Enter the DA in percentage: "))
tax = int(input("Enter the tax in percentage: "))

hra = salary*hra/100

da = (salary*da/100)
salary += da + hra
tax = salary *tax/100
net = salary - tax

print("The net Salary of employee is: ",net)