"""
avion.py
This file is for the kattis problem Avion
CSCI 110
Author- Emily Stockton
12 April 2020
"""
def blimp():
    codes= []

    for _ in range(5):
        codes.append(input())

    found=False 
    for i in range(5):
        if "FBI" in codes[i]:
            print (i+1, end=' ')
            found=True

    if not found:
            print('HE GOT AWAY!')


# can't figure out test cases
# get error: takes 0 positional arguments, but one was given 
def test_cases():
    assert blimp()==False
    print('all test cases passed')

blimp()

test_cases()