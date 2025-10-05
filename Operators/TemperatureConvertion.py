'''Q7. Write a java program to enter temperature in Fahrenheit and convert to Celsius.
Formula :- cel = (fah - 32) * 5 / 9; '''

temp = float(input("Enter the temperature in Fahrenheit: "))

cel = (temp - 32)*(5/9)

print("The Celsius temperature is: ",cel)