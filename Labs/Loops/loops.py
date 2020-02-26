"""
Lab - Playing with Loops
Updated By: FIXME1
CSCI 110
Date: FIXME2
Program prints geometric shapes of given height with * using loops
"""
import os
import sys

height=int(input('enter number???'))


def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of height with *
    """
    i = 1
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

    # FIXME3 ...
    pass


# FIXME4
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

def square():
 height =0 #int(input("Please Enter any Side of a Square  : "))
i = 0
print("Square Star Pattern") 

while(i < height):
    j = 0
    while(j < height):      
        j = j + 1
        print('*', end = '  ')
    i = i + 1
    print('')

printTriangle()
square()
