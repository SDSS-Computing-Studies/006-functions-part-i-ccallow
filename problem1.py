#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is False, then find the hypotenuse
If the boolean is True, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse(c,a,b):
    #inputs
    #a = float
    #b = float
    # x =True or False
    import math 
    if c == "True":
        x = math.sqrt((a**2) + (b**2))
        return x
    if c == "False":
        if a>b:
            x = math.sqrt((a**2)-(b**2))
            return x
        elif b>a:
            x = math.sqrt((b**2)-(a**2))
            return x

"""
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = input("True or False: ")
x= hypotenuse(c)
print(x)
"""