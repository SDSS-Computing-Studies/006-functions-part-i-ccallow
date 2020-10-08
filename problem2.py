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
    #tuple1 =(x1,y1)
    #tuple2 =(x2,y2)
    #return is distance between coordinates
    a=coor1[0]
    b=coor1[1]
    c=coor2[0]
    d=coor2[1]
    x=a-c
    y=b-d
    dist=(x**2 + y**2)**(1/2)
    dist=round(dist,3)
    return dist

num=distance((2,3),(5,6))
print(num)

