#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(coor1,coor2):
    #inputs
    #tuple1 =(a,b)
    #tuple2 =(c,d)
    #return is distance between coordinates
    a=coor1[0]
    b=coor1[1]
    c=coor2[0]
    d=coor2[1]
    x=a-c
    y=b-d
    distance= (x**2 + y**2)**(1/2)
    return distance


coor1=[]
coor2=[]
a=int(input("Enter x value: "))
coor1.append(a)
b=int(input("Enter y value: "))
coor1.append(b)
c=int(input("Enter x value: "))
coor2.append(c)
d=int(input("Enter y value: "))
coor2.append(d)
x = distance(coor1,coor2)
print(x)