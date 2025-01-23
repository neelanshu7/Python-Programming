# D. Create a Python program for a simple console-based Rock-Paper-Scissors game where a user can play against the computer.

'''
Constraints:
> The program should provide a menu for the user to select Rock, Paper, or Scissors.
> The computer's choice should be randomly generated.
> The game should implement the standard Rock-Paper-Scissors rules:
    Rock crushes Scissors.
    Scissors cut Paper.
    Paper covers Rock.
> The program should display the user's choice, the computer's choice, and the result of the round.
> The game should continue until the user chooses to exit.
> Implement input validation to handle invalid choices from the user.
'''

import random as r

while True:
    print("Welcome to Rock-Paper-Scissors Game!")
    print("1. Rock \n 2. Paper \n 3. Scissors \n 4. Exit \n")
    
    user_choice=int(input("Enter your choice(1-4)"))
    # Display user choice
    if user_choice==1:
        print("You choose Rock")
    elif user_choice==2:
        print("You choose Paper")
    elif user_choice==3:
        print("You choose Scissors")
    elif user_choice==4:
        print("Exited Successfully")
        break
    else:
        print("Invalid Input")

    comp_choice=r.randint(1,3)
    # Display Computer  choice
    if comp_choice==1:
        print("Computer choose Rock")
    elif comp_choice==2:
        print("Computer choose Paper")
    elif comp_choice==3:
        print("Computer choose Scissors")
    else:
        print("Invalid Input")

    # Winner Code
    if(user_choice==comp_choice):
        print("Draw")
    else:
        if user_choice==1:
            if comp_choice==2:
                print("Paper covers Rock.")
                print("Computer Win !!")
            else:
                print("Rock crushes Scissors.")
                print("You Win !!")
        elif user_choice==2:
            if comp_choice==1:
                print("Paper covers Rock.")
                print("You Win !!")
            else:
                print("Scissors cut Paper.")
                print("Computer Win !!")
        elif user_choice==3:
            if comp_choice==1:
                print("Rock crushes Scissors.")
                print("Computer Win !!")
            else:
                print("Scissors cut Paper.")
                print("You Win !!")

        # ask the user if they want to play again or exit.
        user_ask=input("Do you want to play again !! (yes/no)")
        if user_ask=='yes' :
            continue
        elif user_ask=='no':
            break
    print("\n\n")
