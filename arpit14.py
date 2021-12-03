"""

a=9
b=8
c=sum((a,b))
print(c)

def function1():
    print("hello you are in function 1")
print(function1())


def fun(a,b):
    average=(a+b)/2
    print(average)
print(fun(5,6))

def function(a,b):
    average=(a+b)/2
    print(average)
v=function(5,6)
print(v)

def function(a,b):
    average=(a+b)/2
    print(average)
    return average
v=function(5,6)
print(v)

def function():
    a=int(input("enter a"))
    b=int(input("enter b"))
    average=(a+b)/2
    print(average)
    return average
function()
"""
def function(a,b):
    """ This is a fuction to calculate avg of two numbers"""
    average=(a+b)/2
    print(average)
    return average
v=function(5,6)
print(v)
print(function.__doc__)
