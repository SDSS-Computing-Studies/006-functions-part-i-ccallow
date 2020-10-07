#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

def perimeter(myList):
    #inputs
    #list = listNumbers
    #return is sum of numbers in listNumbers
    x = sum(myList)
    return x

a = [3, 6, 9, 6]
b = perimeter(a)
print(b)