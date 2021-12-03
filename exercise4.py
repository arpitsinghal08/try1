                            # EXERCISE 3
# PATTERN PRINTING
# input =integer n
# boolean = true or false
# true
# *
# **
# ***
# ****
#  for false pattern reverse

# def function():
#     print("enter number of rows wanted")
#     var1=int(input())
#     pattern=var1*("*"),(var1-1)*("*")
#     if ((var1-1)==0):
#         print(pattern)
# function()


# def function():
#     print("enter number of rows")
#     n=int(input())
#     pattern=n*("*"), (n-1)*function()
#     print(pattern)

# function()

# def function(n):
#     print("number of rows",n)
#     pattern=

# print("enter number of rows")
# var1=int(input())
# while(1):
#     print(var1*int("*")+1)
#     if ((var1-1)==0):
#         break
#     else:
#         continue


# print("how many rows you want to be printed?")
# var1=int(input())
# print("type 1 or 0")
# var2=int(input())
# if var2==1:
#     for i in range(1,var1+1):
#         print("*",int(i))



print("rows?")
var1=int(input())
print("type 1 or 0")
var2=int(input())
boolean=bool(var2)
if boolean==True:
    for i in range(1,var1+1):
        print(i*"*")

if boolean==False:
    for i in range(var1,0,-1):
        print(i*"*")


















