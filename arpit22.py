# #lamda and anonymous funtion
# #
# # def add(a,b):
# #     sum =a+b
# # var1=int(input("enter a"))
# # var2=int(input("enter b"))
# # print(var1+var2)
#
# #
# # minus=lambda x,y: x-y
# #
# #
# # def minus(x,y):
# #     return x-y
# # var1=int(input("enter x"))
# # var2=int(input("enter b"))
# # print(minus(var1,var2))
# #
# #
# # def add(a,b):
# #     return a+b
# # var1=int(input("enter a"))
# # var2=int(input("enter b"))
# # print(add(var1,var2))
#
# minus = lambda x,y:x-y
# var1=int(input("enter your x"))
# var2=int(input("enter y"))
# print(minus(var1,var2))
#
#
# def afunction(a):
#     return a[0]
#
# a=[[1,4],[6,2],[8,23]]
# a.sort(key=afunction)
# print(a)


# afunction=lambda x:x[1]
#
# a=[[1,4],[6,2],[8,25]]
# a.sort(key=afunction)
# print(a)

a=[[1,4],[6,2],[8,23]]
a.sort(key=lambda x:x[1])
print(a)