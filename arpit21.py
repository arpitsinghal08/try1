#recursion (function inside function)
# iterative


#below is example of iterative

# def factorial(n):
#     fac=1
#     for i in range(0,n):
#         fac=fac*(i+1)
#     return fac
#
# var1=int(input("enter your number"))
# print(factorial(var1))

# below is recusive approach

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
var1=int(input("enter your number"))
print(factorial(var1))


def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

var1=int(input("enter your number"))
print(factorial(var1))

