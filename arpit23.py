#EXTERNAL AND BUILTIN MODULES


import random


# randomnumber=random.randint(0,5)
# print(randomnumber)

# randomnumber=random.random()*100
# print(randomnumber)

# list=["star plus","pogo","cn","aaj tak"]
# ran=random.choice(list)
# print(ran)

#EXTERNAL MODULE
# from PyDictionary import PyDictionary
#
# dictionary=PyDictionary()
# x=input("enter the word you wnat to search\n")
# print(dictionary.meaning(x))

# print("let us explore functions inside a module")
# import random
# # a=random.randint(0,10)
# # print(a)
# # a=random.random()
# # print(a)
# # a=random.randrange(10,15)
# # print(a)
# a=random.randbytes(5)
# print(a)
#
# from pandas import pandas as pd
# a=[87,90,43,21]
# a.sort()
# var=pd.Series(a)
# print(var)

# import math
# nan = math.isnan(50)#nan means not a number
# power = math.pow(2 , 5)#pow means power
# # list
# arr = [1, 2, 3, 4, 5]    # [ we have to give a list or tuppel for it
# product = math.prod(arr) #   and this is the syntax for it ]
# remainder = math.remainder(5,2) #gives int remainder
# square_root = math.sqrt(25)
# #issquare_root = math.isqrt(16) #above one will also work the same one.
# print(nan)
# print(power)
# print(product)
# print(remainder)
# print(square_root)


# import math
#
# e = 'please use only available index!!!'
# dict = {'1':'Addition',
#         '2':'Subtraction',
#         '3':'Division',
#         '4':'Reminder',
#         '5':'Multiply',
#         '6':'Greatest common divisor(gcd)',
#         '7':'log',
#         '8':'ln',
#         '9':'logarithm (for unknown base)',
#         '10':'Sine function',
#         '11':'Cosine function',
#         '12':'Tangent function',
#         '13':'Absolute',
#         '14':'Degree --> radian',
#         '15':'Radian --> degree',
#         '16':'Permutation',
#         '17':'Combination',
#         '18':'Factorial',
#         '19':'Power of exp.',
#         '20':'power of unknown number',
#         '21':'Square root'}
# while(1):
#         print('*************************CALCULATOR*************************')
#         for key in dict:
#                 print(key + ' : ' + dict[key])
#         i = int(input('Choose operation using its index:'))
#         if i == 1:
#                 print('Addition:.')
#                 a = input('First number:\n')
#                 b = input('Another number:\n')
#                 for i in range(1, 101):
#                         a = float(a) + float(b)
#                         c = input('You want to add more:\n (y/n):  ')
#                         if c == 'y' or c == 'Y':
#                                 b = input('Another number:\n')
#                         elif c == 'n' or c == 'N':
#                                 print('=\t' + str(a))
#                                 break
#         elif i == 2:
#                 print('Subtraction:.')
#                 a = input('First number:\n')
#                 b = input('Another number:\n')
#                 for i in range(1, 101):
#                         a = float(a) - float(b)
#                         c = input('You want to subtract more:\n (y/n):  ')
#                         if c == 'y' or c == 'Y':
#                                 b = input('Another number:\n')
#                         elif c == 'n' or c == 'N':
#                                 print('=\t' + str(a))
#                                 break
#         elif i == 3:
#                 print('Division:.')
#                 a = input('First number:\n')
#                 b = input('Another number:\n')
#                 for i in range(1, 101):
#                         a = float(a) / float(b)
#                         c = input('You want to divide further:\n (y/n):  ')
#                         if c == 'y' or c == 'Y':
#                                 b = input('Another number:\n')
#                         elif c == 'n' or c == 'N':
#                                 print('=\t' + str(a))
#                                 break
#         elif i == 4:
#                 print('Reminder:.')
#                 a = float(input('First number:\n'))
#                 b = float(input('Another number:\n'))
#                 c = math.fmod(a, b)
#                 print('=\t' + str(c))
#         elif i == 5:
#                 print('Multiplication:.')
#                 a = input('First number:\n')
#                 b = input('Another number:\n')
#                 for i in range(1, 101):
#                         a = float(a) * float(b)
#                         c = input('You want to multiply further:\n (y/n):  ')
#                         if c == 'y' or c == 'Y':
#                                 b = input('Another number:\n')
#                         elif c == 'n' or c == 'N':
#                                 print('=\t' + str(a))
#                                 break
#         elif i == 6:
#                 print('GCD:.')
#                 a = input('First number:\n')
#                 b = input('Another number:\n')
#                 for i in range(1, 101):
#                         a = math.gcd(int(a),int(b))
#                         c = input('You want to another number in it:\n (y/n):  ')
#                         if c == 'y' or c == 'Y':
#                                 b = input('Another number:\n')
#                         elif c == 'n' or c == 'N':
#                                 print('=\t' + str(a))
#                                 break
#         elif i == 7:
#                 print('log 10 base:.')
#                 a = float(input('Enter number for log 10 base:\n'))
#                 b = math.log10(a)
#                 print('=', str(b), sep=' ')
#         elif i == 8:
#                 print('ln/log e base:.')
#                 a = float(input('Enter number for log e base:\n'))
#                 b = math.log1p(a-1)
#                 print('=', str(b), sep=' ')
#         elif i == 9:
#                 print('log for unknown base:.')
#                 b = float(input('Enter base of log function:\n'))
#                 a = float(input('Enter number for log 10 base:\n'))
#                 c = math.log(a, b)
#                 print('=', str(c), sep=' ')
#         elif i == 10:
#                 print('Sin function:.')
#                 a = int(input("Enter:\n '1' for Radian input\n '2' for degree input: "))
#                 if a == 1:
#                         b = float(input('Radian:\n'))
#                         c = math.sin(b)
#                         print('=', str(c), sep=' ')
#                 elif a == 2:
#                         b = float(input('Degree:\n'))
#                         c = math.sin(math.radians(b))
#                         print('=', str(c), sep=' ')
#         elif i == 11:
#                 print('Cos function:.')
#                 a = int(input("Enter:\n '1' for Radian input\n '2' for degree input: "))
#                 if a == 1:
#                         b = float(input('Radian:\n'))
#                         c = math.cos(b)
#                         print('=', str(c), sep=' ')
#                 elif a == 2:
#                         b = float(input('Degree:\n'))
#                         c = math.cos(math.radians(b))
#                         print('=', str(c), sep=' ')
#         elif i == 12:
#                 print('Tan function:.')
#                 a = int(input("Enter:\n '1' for Radian input\n '2' for degree input: "))
#                 if a == 1:
#                         b = float(input('Radian:\n'))
#                         c = math.tan(b)
#                         print('=', str(c), sep=' ')
#                 elif a == 2:
#                         b = float(input('Degree:\n'))
#                         c = math.tan(math.radians(b))
#                         print('=', str(c), sep=' ')
#         elif i == 13:
#                 print('Absolute:.')
#                 a = float(input('Enter a number:\n'))
#                 b = math.fabs(a)
#                 print('=', str(b), sep=' ')
#         elif i == 14:
#                 print('Degree to radian:.')
#                 a = float(input('Degree:\n'))
#                 b = math.radians(a)
#                 print('=', str(b), sep=' ')
#         elif i == 15:
#                 print('Radian to degree:.')
#                 a = float(input('Radian:\n'))
#                 b = math.degrees(a)
#                 print('=', str(b), sep=' ')
#         elif i == 16:
#                 print('Permutation (n!/(n-k)!):.')
#                 a = int(input("Enter 'n':.\n"))
#                 b = int(input("Enter 'k':.\n"))
#                 c = math.perm(a, b)
#                 print('=', str(c), sep=' ')
#         elif i == 17:
#                 print('Combination (n!/((n-k)!*k!)):.')
#                 a = int(input("Enter 'n':.\n"))
#                 b = int(input("Enter 'k':.\n"))
#                 c = math.comb(a, b)
#                 print('=', str(c), sep=' ')
#         elif i == 18:
#                 print('Factorial (n!):.')
#                 a = int(input("Enter 'n':\n"))
#                 b = math.factorial(a)
#                 print('=', str(b), sep=' ')
#         elif i == 19:
#                 print('Power of exponent:.')
#                 a = float(input('Enter power of e:\n'))
#                 b = math.exp(a)
#                 print('=', str(b), sep=' ')
#         elif i == 20:
#                 print('Power of Unknown:.')
#                 a = float(input('Enter base:\n'))
#                 b = float(input('Enter power:\n'))
#                 c = math.pow(a, b)
#                 print('=', str(c), sep=' ')
#         elif i == 21:
#                 print('Square root:.')
#                 a = float(input('Enter a number:\n'))
#                 b = math.sqrt(a)
#                 print('=', str(b), sep=' ')
#         else:
#                 print('You are doing some mistake\nplease, choose only index corresponds to operations.')
#         x = input('You want reuse CalC.\n(y/n):\t\t')
#         if x=='y' or x=='Y': continue
#         elif x=='n' or x=='N': break
#         else: print('You are doing some mistake\nplease, choose only index corresponds to operations.')
# print("Thank U")

