#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
def isInteger(x):
    #inputs
    #x = float
    #return True if a is an integer
    #return False if a is not an integer
    if x == int(x):
        return True
    elif x != int(x):
        return False
    

a = float(input("Enter a number: "))
b = isInteger(a)
print(b)
