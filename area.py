import math

def area_of_rectangle(length,width):
    return length * width
    
def area_of_triangle(height,base):
    return 0.5 * base * height
    
def area_of_circle(radius):
    return math.pi * r ** 2
    
print("For Calculating Area of Rectangle, enter : ")
length = int(innpt("Length of Rectangle : "))
width = int(input("Width of Rectangle : "))
print(f"Area of Rectangle : {area_of_rectangle}")
print()

print("For Calculating Area of Triangle, enter : ")
height = int(input("Height of Triangle : "))
base = int(input("Base of Triangle : "))
print(f"Area of Triangle : {area_of_triangle}")
print()

print("For Calulating Area of Circle, enter : ")
radius = int(input("Radius of Circle : "))
print(f"Area of Circle : {area_of_circle}")
print()
