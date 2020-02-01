# triangle.py- By: Date- 31 Jan 2020
# this program calculates and displays the perimeter and area of a triangle given 3 sides

#Algorithim Steps
# 1. Prompt user for side a, side b, and side c
# 2. Store side a,b,c as variables
# 3. Calculate perimeter with a+c+c=p
# 4. Calculate area with formulae s=(a+b+c)/s
#     a=sqrt(s(s-a)(s-b)(s-c))
# 5. display output 

#import math library 
import math

print('This program will compute the area and perimeter of a triangle')
side_a=input('Enter side a')
side_a=int(side_a)

side_b=input('Enter side b')
side_b=int(side_b)

side_c=input('Enter side c')
side_c=int(side_c)

Perimeter=side_a+side_b+side_c
print('The perimeter is',Perimeter)
s=Perimeter/2

Area=math.sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
print('The area is',Area)