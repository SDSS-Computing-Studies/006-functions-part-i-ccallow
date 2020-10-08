#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(myList):
    #inputs
    #myList = list
    # #return value is largest number
    myList.sort()
    x = str(myList[-1])
    return x

"""
y = [3,8,12,9]
a = largest(y)
print(a)
"""