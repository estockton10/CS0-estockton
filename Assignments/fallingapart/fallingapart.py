"""
File name- fallingapart.py
this file is for the kattis problem falling apart (https://open.kattis.com/problems/fallingapart)
Date- 17 April 2020
Author- 
CSCI 110

"""
def game():
    n = int(input())

    l = [int(x) for x in input().split()]
    alice = 0
    bob = 0

    while l:
        alice += max(l)
        l.remove(max(l))
        if l:
            bob += max(l)
            l.remove(max(l))

    print (alice, bob)

game()
