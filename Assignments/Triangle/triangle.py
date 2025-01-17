""" triangle.py- By: Emily Stockton
#  Date- 31 Jan 2020
# This program calculates and displays the perimeter and area of a triangle given 3 sides

#Algorithim Steps
# 1. Prompt user for side a, side b, and side c
# 2. Store side a,b,c as variables
# 3. Calculate perimeter with a+b+c=perimeter
# 4. Calculate area with formulae s=(a+b+c)/s &
#     a=sqrt(s(s-a)(s-b)(s-c))
# 5. Determine if valid triangle
# 6. display output 
"""
#import math library 
import math

#promt user for side lengths
print('This program will compute the area and perimeter of a triangle when given the length of 3 sides')
a=float(input('Enter length of side a'))


b=float(input('Enter length of side b'))


c=float(input('Enter length of side c'))



#calculate perimeter & area
Perimeter=a+b+c
print('The perimeter is',Perimeter)
s=Perimeter/2



#determine if valid triangle
if (s*(s-a)*(s-b)*(s-c))<=0:
    print('These sides do not make a valid triangle')
else: 
  Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
  print('The area is',Area)
  