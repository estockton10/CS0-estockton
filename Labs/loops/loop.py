"""
Lab - Playing with Loops
Updated By: Emily Stockton
CSCI 110
Date: 4 March 2020
Program prints geometric shapes of given height with * using loops
"""
import os
import sys





def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of height with *
    """
    #height=int(input('enter number???'))
    i = 0
    while i <= height:
        print('*  '*i)
        i += 1
    print('')  # print an empty line


def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(height):
        for j in range(height-i):
            print('* ',end="")
        print('')
    print('')    


    # FIXME3 ... #fixed#



# FIXME4 #fixed#
# Design and implement a function that takes a number as height and
# prints square of the given height with *.
# Square of height 5, e.g., would look like the following.
"""
*  *  *  *  *  
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
"""
##output square pattern
def print_square(height):
 #int(input("Please Enter any Side of a Square  : "))
    i = 0
    while(i < height):
            j = 0
            while(j < height):      
                j = j + 1
                print('*', end = '  ')
            i = i + 1
            print('')



def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    # FIXME7 add a loop to make the program to continue to run until the user wants to quit #fixed#
    # FIXME8 call clearScreen function to clear the screen for each round of the loop #fixed
    while True:
        print('Program prints geometric shapes of given height with *')
        height = int(input('Please enter the height of the shape: '))
        printTriangle(height)
         
        # FIXME5 #fixed#
        # Call printFlippedTriangle passing proper argument
        # Manually test the function
        printFlippedTriangle(height)


    # FIXME6 #fixed#
    # Call the function defined in FIXME4 passing proper argument
    # Manually test the function
        print_square(height)

    # FIXME9 #fixed#
    # prompt user to enter y/Y to continue anything else to quit

    # FIXME10#fixed#
    # Use conditional statements to break the loop or continue in the loop
        answer = input("Would you like to print more star patterns? [Y|N]")
        if answer == 'y':
            continue
        elif answer=='Y':
            continue
        else:
            break


main()

    # FIXME5
    # Call printFlippedTriangle passing proper argument
    # Manually test the function

    # FIXME6
    # Call the function defined in FIXME4 passing proper argument
    # Manually test the function

    # FIXME9
    # prompt user to enter y/Y to continue anything else to quit

    # FIXME10
    # Use conditional statements to break the loop or continue in the loop
