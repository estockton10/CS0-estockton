"""
Lab - String
By: Emily Stockton

CSCI 110
Date: 30 March 2020

Program prompts user to enter a phrase and tells the user various properties about the phrase.
"""

import sys
import string


def isReversible(phrase):
    # Function to determine whether given phrase is same forward and backward, i.e.,
    # reversible or not.
    length = len(phrase)  # get the length of phrase
    reversible = True  # lets assume every phrase is reversible!
    j = length - 1 # right index
    for i in range(0, length, 1):  # start at 0 end at length-1, step to increment is 1
        # Algorithm steps:
        # 1. go through each character
        #       a. ignore all the non-alphabetic characters on both ends of the phrase
        # 2. compare the corresponding
        #     characters from left and right of the phrase
        # 3. if a single pair is not equal
        #     the phrase is NOT reversible
        # 4. else, if all the pairs are same, the word is reversible
        if not phrase[i].isalpha():
            continue
        while not phrase[j].isalpha():
            j -= 1
            if j < 0: #if passed the first letter; return False or not reversible
                return True

        if phrase[i] != phrase[j]:
            reversible = False
            break
        j -= 1

    return reversible


def hasLowerCase(phrase):
    for i in range(len(phrase)):
        if phrase[i].islower():
            return True
    return False


def hasUpperCase(phrase):
    for ch in phrase:
        if ch.isupper():
            return True
    return False


def hasDigit(phrase):
    # FIXME1: return True if phrase has at least 1 digit, false otherwise
    for ch in phrase:
        if ch.isdigit():
            return True
    return False


def hasSymbol(phrase):
    # FIXME2: return True if phrase has at least one of these symbols: ~!@#$%
    for ch in phrase:
    # return False otherwise
   #pass


def main():
    print("Program tells various properties of a given phrase")

    while True:
        phrase = input("Enter a word or phrase: ")

        if isReversible(phrase):
            print("{} is reversible!".format(phrase))
        else:
            print("{} is not reversible!".format(phrase))

        # FIXME - # FIXED #
        # print if the phrase has a upper case character by calling the proper function
        if hasUpperCase(phrase):
            print('{} has an upper case character.'.format(phrase))
        else:
            print('{} does not have an upper case character.'.format(phrase))

        # FIXME3 #FIXED#
        if hasLowerCase(phrase):
            print('{} has a lowercase character'.format(phrase))
        else:
            print('{} does not have a lowercase character'.format(phrase))
    
        # print if the phrase has a lower case character by calling the proper function

        # FIXME4 #FIXED#
        if hasDigit(phrase):
            print('{} has a digit.'.format(phrase))
        else:
            print('{} does not have a digit'.format(phrase))
        # print if the phrase has a digit by calling the proper function

        # FIXME5
        if hasSymbol
        # print if the phrase has a symbol by calling the proper function

        ans = input('Want to continue? [y/n]: ')
        ans = ans.lower()
        #continue of user enters yes or Yes or y or anything that starts with y
        if ans.startswith('y'): 
            continue
        else:
            print('Good bye!')
            break

def test():
    print('run unit test cases...')
    assert isReversible('race car!') == True
    assert isReversible('jeep!') == False
    assert hasLowerCase('Welcome!') == True
    assert hasLowerCase('ABC235!') == False
    assert hasUpperCase('WELcome!!') == True
    assert hasUpperCase('$!#%#@asdfdsf') == False
    assert hasDigit('22424ADSFDS') == True
    assert hasDigit('asdfdsfWASDFASDG') == False
    assert hasSymbol('!@$DAD$%') == True
    assert hasSymbol('asdfASF3424') == False
    print('all test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test()
    else:
        main()