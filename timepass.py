#prime number

# var1=int(input("enter your number\n"))
# if (var1>1):
#     for i in range(2,var1):
#         if var1%i==0:
#             print(var1,"is not a prime number")
#             break
#         else:
#             print(var1,"it is a prime number ")
#             break
#
# else:
#     print(var1,"it is not  a prime number")

#sum of quares of first n natural numbers


# var1=int(input("enter n\n"))
#
# def function(n):
#     return (n*(n+1)*(2*n+1))/6
#
# print(function(var1))

# sum of cubes of first n natural numbers

# var1=int(input("enter n\n"))
#
# def function(n):
#     return ((n*(n + 1)) / 2)**2
# print(function(var1))



# program to interchange first and last element of a list

#
# list1=[1,2,3,4,5,6,7,8,9]
# def swaplist(list):
#     var1=list.pop(0)
#     var2=list.pop()
#
#     list.insert(0,var2)
#     list.append(var1)
#
#     return list
#
# print(swaplist(list1))

# swap 2 element of a list


# list1=[1,2,3,4,5,6,7,8]
#
#
# var1=int(input("enter the number's position to be swapped"))
# var2=int(input("enter the number to be swapped with"))
#
# def function(list):
#     var3=int(list.pop(var1))
#     var4=int(list.pop(var2-1))
#
#     list.insert(var1,var4)
#     list.insert(var2,var3)
#
#     return list
#
# print(function(list1))

# sum of elements in a list

import math

# list=[1,2,3,4,56]
# sum1=sum(list)
# print(sum1)

#finding nth largest number in a list


# list=[1,2,3,4,56]
# size=int(len(list))
# list.sort()
# print(list[size-2])



# printing even numbers in a range:
# var1=int(input("enter starting value of range"))
# var2=int(input("enter ending value of range"))
#
# for i in range(var1,var2+1):
#     if i%2==0:
#         print(i)


# printing negative numbers of a list

# list=[1,2,3,4,-2]
#
# for item in list:
#     if item<0:
#         print(item)
# counting occurance of a element in a list
# list=[1,23,3,3,3,4,5]
# v=list.count(1)
# print(v)


#check if a string is palindrome or not
"""

var1=str(input("enter your word\n"))
if var1==var1[::-1]:
    print("word is palindrome ")
else:
    print("word is not palindrome")

"""

#reversing words in a string
# var1=str(input("enter your word\n"))
# print(var1[::-1])

#removing ith caracter
# var1=str(input("enter your word\n"))
# var2=int(input("enter the number of  the character to be removed"))
# print(var1.replace(var1[var2],""))


#printing evn length words of a string        ***
"""
var1=str(input("enter your string\n"))

def printeven(s):
    s=s.split(" ")

    for word in s:
        if len(word)%2==0:
            print(word)

printeven(var1)
"""
# accept strings which contain all vowels
# var1=str(input("enter string\n"))
# s1=set(["a","e","i","o","u"])
# s2=set(var1)
# s3=set(s1.intersection(s2))
# if s3==s1:
#     print("accepted")
#
# else:
#     print("not accepted")

# counting number of matching characters in a pair of string
"""
var1=str(input("enter 1st string\n"))
var2=str(input("enter 2nd string\n"))
s1=set(var1)
s2=set(var2)
s3=s1.intersection(s2)
print(s3)
print(len(s3))

"""
#finding element of max/min occurance
"""
from collections import Counter
var1=str(input("enter string\n"))
var2=Counter(var1)
var2=max(var2,key=var2.get)
print(str(var2))
"""

