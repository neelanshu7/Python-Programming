"""
A. Write a Python program to exhibit the functional behavior of all the arithmetic
operators (+, -, *, /, //, **) and their order of precedence.
"""
a=int(input("Enter value for a"))
b=int(input("Enter value for b"))
c=int(input("Enter value for c"))

print("Arithematic Operations : ")

print("Addition : ",a+b)
print("Substraction : ",a-c)
print("Multiplication : ",a*b)
print("Division : ",a/b)
print("Floor Division : ",b//c)

print("Order of Precedence")
print("Operation 1 : ",a+b*c)
print("Operation 2 : ",(a+b)*c)
print("Operation 3 : ",a**c+b)
print("Operation 4 : ",a+b//c)
print("Operation 5 : ",(a+b)//c)
print("Operation 6 :",(a+b)//c*a)
