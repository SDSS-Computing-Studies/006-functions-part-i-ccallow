#!python3

def sum(a,b):
    #inputs
    # a : float 
    # b : float
    # return value: returns the sum of the 2 numbers
    x= a+b
    return x
    
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

x = sum(a,b)
print(x)
