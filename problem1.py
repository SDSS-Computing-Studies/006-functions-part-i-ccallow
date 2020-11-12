#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is False, then find the hypotenuse
If the boolean is True, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math 
def hypotenuse(a,b,c):
    #inputs
    #a = float
    #b = float
    # x =True or False
    if c ==True:
        x = (a**2) + (b**2)
        y = int(math.sqrt(x))
        return y
    elif c == False:
        if a>b:
            x = (a**2)-(b**2)
            y = int(math.sqrt(x))
            return y
        elif b>a:
            x = (b**2)-(a**2)
            y = math.sqrt (x)
            return y

"""
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = input("True or False: ")
x= hypotenuse(c)
print(x)
"""
