"""
Create a Python module named marks_Calculator that encapsulates functionalities
for students' marks computation in different subjects. Within this module, design a functon that:
"""
#a. Takes inputs and calculates the total marks obtained by a student in various subjects.
#b. Computes the average marks and grade obtained by the student across all subjects.
#c. Returns the calculated average marks and grade.

import marks_Calculator as m

print("Enter Subject-wise marks of CIA-1")
python=int(input("Enter Marks obtained in Python"))
cn=int(input("Enter Marks obtained in Computer Networks"))
dwdm=int(input("Enter Marks obtained in Data Warehouse & Data Mining"))
isrt=int(input("Enter Marks obtained in Information Storage & Retrival Techniques"))
linux=int(input("Enter Marks obtained in Linux Programing & Scripting"))

marks=[python,cn,dwdm,isrt,linux]

stu = m.student(marks)

print("Average Marks ",stu[0])
print("Grade ",stu[1])
