"""
I. Create a Python program that takes two strings as input and determines if the second
string is a substring of the first one.
"""

s1=input("Enter first String : ")
s2=input("Enter second String : ")
print("\n")

print("First String is : ", end=" ")
for i in  range(len(s1)):
    print(s1[i],end="")
print("\n")

print("Second String is : ", end=" ")
for i in  range(len(s2)):
    print(s2[i],end="")
print("\n")

if s2.lower() in s1.lower():
    print("Yes")
else:
    print("No")
