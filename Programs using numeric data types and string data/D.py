# D. Write a python program to calculate area of circle, rectangle and triangle

# For Circle 
print("Circle Details")
r=float(input("Enter radius of Circle"))
a_circle=3.14*r*r

print("Rectrangle Details")
l=float(input("Enter lenght of Rectrangle"))
b=float(input("Enter breadth of Rectrangle"))
a_rect=l*b

print("Triangle Details")
base=float(input("Enter base of Triangle"))
height=float(input("Enter height of Triangle"))
a_triangle=(1/3)*base*height

print("Area of Circle",a_circle)
print("Area of Rectrangle",a_rect)
print("Area of Triangle",a_triangle)
