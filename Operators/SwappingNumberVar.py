'''Q14. Write a python program swap two number using third variable. '''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping")
print("a is: ",a)
print("b is: ",b)

print("After Swapping")
# logic of swappping using third variable
temp = a 
a = b
b = temp

print("a is: ",a)
print("b is: ",b)