#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 18, 2025
# This program is a immitation of gambling, you need to guess the number from 0 to 9

import random


def main():
    try: 
        #Gets the input number from user
        user_number = float(input("Insert random number from 0 to 9"))
        #Generates random number
        computer_number = random.uniform(0, 9)
        #The if function compares the answer of user with computer
        if user_number == computer_number:
            #If user inserted correct number he will recieve this message
            print("You won.")
        elif user_number != computer_number:
            #Will insert the specific message if the user input is incorrect
            print("Couldn't be me loser, the number is {}".format(computer_number))
            #Shows this phrase if the program will see string or boolean variable. 
    except ValueError:
        print("I outsmarted you.")


if __name__ == "__main__":
    main()
