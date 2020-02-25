#########################
#File name: functions.py 
#This file takes two numbers and finds the sum,differecene,product,quotient,remainder 
# and finds the largest of the two numbers
#CSCI 110 
#Emily Stockton
#Last modified- 25 Feb 2020
##########################

"""Write program and programmer information at the top of the program as comments (5 points)
Define a function that takes two numbers, adds two numbers and returns the sum (5 points)
Define a function that takes two numbers, multiplies the two numbers and returns the product (5 points)
Define a function that takes two numbers; divides the first number by the second and returns the quotient (5 points)
Define a function that takes two numbers, subtracts the second from the first and returns the difference (5 points)
Define a function that takes two numbers, finds and returns the remainder of the first number divided by the second (5 points)
Define a function that takes two numbers, finds the first to the power of the second number and returns the value (5 points)
Define a function that takes a number and returns the square-root of the number (5 points)
Prompt the user to enter two numbers (5 points)
Call all the functions passing those two entered numbers and print the calculated results with proper descriptions (15 points)
Write 2 tests cases using assert statements to automatically test each function. (5*7 = 35 points)
Update README.md file with the status of the project and self grade. (5 points)
Bonus 10 points - Write a function that finds and returns the larger of two given numbers. Call function to test it with the same two numbers.
"""



import math

#Define addition function
def add(num1,num2):
    return int(num1) +int(num2)
    

#define multiply function
def multiply(num1,num2):
    return int(num1) *int(num2)


#define divide function
def divide(num1,num2):
    return float(num1)//float(num2)



#define subtract function
def subtract(num1,num2):
    return float(num1)-float(num2)



#define remainder
def remainder(num1,num2):
    return int(num1)%int(num2)



#define power function
def power(num1,num2):
    return float(num1)**(num2)



#define sqrt
def sqrt(num2):
    return (num2**0.5)



#function to find larger of two numbers
def greaterthan(num1,num2):
    if num1<num2:
       result= num2
    
    elif num1>num2:
         result=num1
    
    else:
        result='the numbers are eqaul'
    
    return result


#test funcitons
def testFunction():
    assert (add(5,5)==10)
    assert (add(5,3)==8)
    assert (multiply(5,5)==25)
    assert(multiply(5,3)==15)
    assert(divide(6,2)==3)
    assert(divide(8,4)==2)
    assert(remainder(7,5)==2)
    assert(remainder(5,4)==1)
    assert(power(2,8)==256)
    assert(power(2,2)==4)
    assert(sqrt(9)==3)
    assert(sqrt(16)==4)
    assert(greaterthan(2,1)==2)
    print('all test functions passed')

#call test functions
testFunction()



#ask user for 2 numbers
num1=float(input("Enter a number: "))
num2=float(input("Enter a second number: "))

#output results
print('The sum of your numbers is:',add(num1,num2))
print('The product of your numbers is:',multiply(num1,num2))
print('The quotient of your numbers is:',divide(num1,num2))
print('The difference of your numbers is:',subtract(num1,num2))
print('The remainder of your numbers is:',remainder(num1,num2))
print('first number to the power of the second number is:',power(num1,num2))
print('The square root of your first number is:',sqrt(num1))
print('The square root of your second number is:',sqrt(num2))
print('The larger of the two numbers is:',greaterthan(num1,num2))


