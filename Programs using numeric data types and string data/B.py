"""
B. Write a python program to convert Fahrenheit to Celsius and vice versa.
"""
cel=float(input("Enter temprature in Celcius "))
far = cel*(9/5)+32
print(far)

far1=float(input("Enter temprature in Fahrenheit "))
cel1 = (far1-32)*(5/9)
print(cel1)
