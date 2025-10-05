''' Q9. Write a java program to enter two angles of a triangle and find the third angle.  '''

angle1 = int(input("Enter the first angle of triangle: "))
angle2 = int(input("Enter the second angle of triangle: "))

angle3 = 180 - (angle1 + angle2)

print("Third angle is: ",angle3)