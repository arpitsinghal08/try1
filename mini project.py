# #MINI PROJECT
# # LIBRARY CLASS
# # DISPLAY LEND DONATE RETURN BOOK
# # DICTIONARY FOR LENDING(NAMEOF BOOK:PERSON WHO HAS BOOK)
#
#
# # CREATE  A MAIN FUNCTION AND RUN AN INFINITE WHILE LOOP ASKING USER FOR THEIR INPUT
# import random
# from pandas import pandas as pd
# randomnumber=random.randint(10,10000)
# print("Hello,welcome to ARPIT library")
#
# print("what are you upto?")
# print("press 1 for viewing books in library\npress 2 for lending a book\npress 3 for donating a book\npress 4 for returning the book")
# var1=int(input())
#
# i=0
# while(1):
#     if var1 == 1:
#         print("these are the books we have:")
#         list = ["bhagvatgita", "my granny", "computer the new world"]
#         var2 = pd.Series(list)
#         print(var2)
#         var7=input("press 1 for any other action \npress0 for finish")
#
#     if var7==1:
#         print("press1 for lending\npress2 for donting\npress 3 returning")
#
#     if var7==0:
#         print("thankyou")
#
#
#     if var1 == 2:
#         print("choose among these books")
#         list = ["bhagvatgita", "my granny", "computer the new world"]
#         var2 = pd.Series(list)
#         print(var2)
#         var3 = str(input())
#         print("congratulations, you have borrowed ", var3, "book")
#         print("your speacial code is ", randomnumber)
#         break
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# if var1==3:
#     print("thank you for helping us!")
#     var4=str(input())
#     print("thank you,you donated",var4,"book")
#     list.append(var4)
#
#
# if var1==4:
#     var5=str(input("enter your name or special code"))




from pandas import pandas as pd
import random
randomnumber=random.randint(10,10000)
class library:
    def __init__(self,listofbooks,libraryname):
        self.listofbooks=listofbooks
        self.libraryname=libraryname





    def displaybooks(self):

        list = ["bhagvatgita", "my granny", "computer the new world"]
        var2 = pd.Series(list)
        print(var2)

    def lendbook(self):
        print("these are the following books we have:-")
        list = ["bhagvatgita", "my granny", "computer the new world"]
        var2 = pd.Series(list)
        print(var2)
        var3=str(input("enter the book name\n"))
        print("Book issued Successfully...")
        print("your special code is:",randomnumber)

    def donatebook(self):
        var4=str(input("enter the book name:"))
        print("thank you !")

    def returnbook(self):
        var5=int(input("enter your speacial code "))
        print("Book returned Successfully...")

arpit=library(["bhagvatgita", "my granny", "computer the new world"],"arpit library")


while True:
    print("What do you want? Please enter your option(1/2/3/4/5):\n1. Display Books "
          "\n2. Lend Book \n3. Add Book\n4. Return book\n5. Quit")
    option = input()

    if option == '5':
        print("Thank You For Your Visit")
        break
    elif option == '1':
        arpit.displaybooks()
    elif option == '2':
        arpit.lendbook()
    elif option == '3':
        arpit.donatebook()
    elif option == '4':
        arpit.returnbook()
    else:
        print("Invalid input, Try again !!!")









