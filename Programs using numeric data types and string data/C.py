# C. Write a python program to calculate simple and compound interest

"""
Formula
SI=P.R.T/100
AMT=P+SI
"""

p=float(input("Enter Principal amount "))
r=float(input("Enter Rate of Intrest "))
t=float(input("Enter Time Period "))

si=(p*r*t)/100
amt= p+si

print("Simple Intrest = ",si)
print("Amount = ",amt)
