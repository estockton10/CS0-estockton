"""
CSCI 110
List Lab

By: Emily Stockton
Date: 14 April 2020

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

totalInts = 10


def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        intList.append(num)  # store num into integers list
        i += 1
    return intList


def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    # FIXME3 (20 points)
    pass


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    printList(integers)
    print()
    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)
    # FIXME4 (10 points)
    # Call sortListInDescendingOrder function
    # FIXME5 (10 points)
    # Print the sorted list in descending order
    # FIXME6 (10 points)
    # Print the largest number
    # FIXME7 (10 points)
    # Print the smallest number
    # FIXME8 (10 points)
    # Find and print the index of the smallest number
    # FIXME9 (10 points)
    # Print the index of the largest number


# FIXME10 (20 points)
# Call main function if this file is run as the main module
print('call main() function to see partial outputs of the program...')

main()