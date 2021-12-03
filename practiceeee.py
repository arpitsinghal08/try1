#write a program in which people
# have to guess the number[18] and you have to guide
# the person to reach tha correct number by telling that
# the number entered is greater or smaller
# maximum number of guesses=9
#print number of guesses left
#after 9 guesses print game over
#number of guesses used

"""
#  var2= number of chances
var2=0
while(var2<=9):
    print("enter your number")
    var1=int(input())
    if var1>18:
        print("greater")
        var2=var2+1
        print("attempt number--",var2)
    if var2>=9:
        print("game over")
        break
        continue
    if var1<18:
        print("smaller")
        var2=var2+1
        print("attempt number--",var2)
    if var2 >=9:
        print("game over")
        break
        continue
    if var1==18:
        print("correct answer you won game over")
        var2=var2+1
        print("attempt number--",var2)
    if var2>=9:
        print("game over")
        break
        continue

def function():
    print("hello")
print(function())
function()


def function1(a,b):
    print("sum",a+b)
print(function1(4,3))
function1(4,3)
"""

def function(a,b):
    average=(a+b)/2
    print(average)
    return average
v=function(2,4)
print(function(2,4))
