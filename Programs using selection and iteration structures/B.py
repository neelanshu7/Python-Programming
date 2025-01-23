# B. Write a python program to calculate Body Mass Index (BMI) based on user input.
"""
bmi = weight / (height ** 2)
bmi less than 18.5, print 'Underweight'
18.5 <= bmi < 25, print 'Normal Weight'
25 <= bmi < 30, print 'Overweight'
Otherwise print 'Obese'
"""
weight=float(input("Enter your Weight : "))
height=float(input("Enter your Height : "))

bmi=weight/(height**2)

print("Your BMI is ",bmi)

if bmi<18.5 :
    print("Under-weight")
elif bmi>=18.5 and bmi<25:
    print("Normal-weight")
elif bmi>25 and bmi<30:
    print("Over-weight")
else:
    print("Obese")
