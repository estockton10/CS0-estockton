###
# Functions lab 
# Updated by: Emily Stockton #fixed#
# Date: 4 Feb 2020 #fixed#
# CSCI 110
# Functions & variable scopes
##

# assign Bill Gates to someName variable
someName="Bill Gates" #global variable

# assign my name to myName
myName="Emily" #fixed# global variable

def printHello():
     """
    function that prints Hello World.
    doesn't take any argument and doesn't return a value
    """
     print("Hello World!")

def printHelloTwice():
    """
     function that prints Hello World twice
     calls printHello function twice
    """
    printHello()
    printHello()

def greetName(name):
    """ 
    function that takes one argument name and greets the name
    """
    print("Hi there {}".format(name))

def meetAndGreet():
    """
    function that greets someone
    doesn't take any argument and doesn't return any value
    """
    firstName=input("\nHey there! What is your first name?\n")
    greetName(firstName) #call greetName function
    print("My name is {}. Nice to meet you.".format(myName))
    print()

def convertTime(seconds):
    """
    #FIXME - #fixed#
    Define a function named convertTime that takes 1 integer argument called seconds.
    The function converts and prints the seconds in hours, minute, and seconds formats.
    """
    hour=seconds//3600
    m=seconds//60
    m=m%60
    sec=seconds%60
    print("{} seconds = {} hours, {} minutes, {} seconds".format(seconds, hour, m, sec))

def findSeconds(hours):
    """
    #FIXME - #fixed#
    Define a function named findSeconds that takes hours as 1 integer argument.
    The function converts hours into seconds and returns it
    """
    #convert hours into seconds and update seconds variable#fixed#
    seconds=hours *3600
    return seconds

def testFunctions():
    #test1: 1 hour==3600 seconds
    assert(findSeconds(1) ==3600)
    # FIXME5 - write 3 more tests cases for findSeconds function#fixed#
    #test2: 24 hours==86400 seconds
    assert(findSeconds(24)==86400)
    #test3:48 hours==172800 seconds
    assert(findSeconds(48)==172800)

    print('all test cases passed')
    
# FIXME6: call printHello function - #fixed#
printHello()

# FIXME7 - call printHelloTwice function #fixed#
printHelloTwice

greetName(someName)  # calling function passing variable as argument
greetName("Larry Page") # calling function passing literal value as argument

# call meetAndGreet function
meetAndGreet()

# call function convertTime passing proper argument
convertTime(60)

# FIXME8 - Call converTime function passing 3600 as seconds #fixed#
convertTime(3600)


# FIXME9 - Call converTime function passing 3661 as seconds #fixed#
convertTime(3661)

#FIXME10-call test functions #fixed$
testFunctions()

