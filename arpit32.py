#     MAP
# number=["3","34","64"]
# for i in range(len(number)):
#     number[i]=int(number[i])
#
# number[2]=number[2]+1
# print(number[2])

# number=["3","34","64"]
# number=list(map(int,number))
# number[2]=number[2]+1
# print(number[2])



# def sq(a):
#     return a*a
# num=[2,3,4,5,6,7]
# square=list(map(sq,num))
# print(square)



# num=[2,3,4,5,6,7]
# square=list(map(lambda x:x*x,num))
# print(square)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func=[square,cube]
#
# for i in range(5):
#     var1=list(map(lambda x:x(i),func))
#     print(var1)


# fILTER FUNCTION
# list1=[1,2,3,4,5,6,7]
# def greater(num):
#     return num>5
#
# greater5=list(filter(greater,list1))
# print(greater5)

#REDUCE

from functools import reduce
list1=[1,2,3,4]
# num=0
# for i in list1:
#     num=num+i
# print(num)

num=reduce(lambda x,y:x+y,list1)
print(num)