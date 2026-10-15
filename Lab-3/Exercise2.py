import math

x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
y1 = float(input("Enter the value of y1: "))
y2 = float(input("Enter the value of y2: "))

d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

print("The distance between two points is " , d)
