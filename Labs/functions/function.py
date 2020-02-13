###
# Functions lab 
# Updated by: 
# Date: 4 Feb 2020
# CSCI 110
#
##

# assign Bill Gates to someName variable
someName="Bill Gates"

# assign my name to myName
myName="Insert Name"

def printHello():
    print("Hello World!")

def printHelloTwice():
    printHello()
    printHello()

def greetName(name):
    print("Hi there {}".format(name))

def meetAndGreet():
    firstName=input("\nHey there! What is your first name?\n")
    greetName(firstName)
    print("My name is {}. Nice to meet you.".format(myName))
    print()

def convertTime(seconds):
    hour=seconds//3600
    m=seconds//60
    m=m%60
    sec=seconds%60
    print("{} seconds = {} hours, {} minutes, {} seconds".format(seconds, hour, m, sec))

def findSeconds(hours):
    seconds=0
    return seconds

def testFunctions():
    assert(findSeconds(1)==3600)
    print('bruh it worked')

printHello
printHelloTwice

meetAndGreet()
convertTime(60)
convertTime(3600)
testFunctions()

