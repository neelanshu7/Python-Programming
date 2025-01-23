# A. Write a Python program to guess a number between 1 and 9.
"""
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt
appears again un7l the guess is correct, on successful guess, user will get a "Well
guessed!" message, and the program will exit.
"""
import random

random_number=random.randint(1,9)

while True:
    user_guess=int(input("Enter a number between 1-9 : "))

    if user_guess<1 or user_guess>9:
        print("Please enter a number between 1-9 : ")
    elif user_guess==random_number:
        print("Well guessed!")
        break
    else:
        print("Not Correct! Try Again")