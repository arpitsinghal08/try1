#write a program in which people
# have to guess the number[18] and you have to guide
# the person to reach tha correct number by telling that
# the number entered is greater or smaller
# maximum number of guesses=9
#print number of guesses left
#after 9 guesses print game over
#number of guesses used

print("maximum number of attempts =9")
#var2 = number of attempts
var2=0
while(var2<=9):
    print("enter your number")
    var1=int(input())
#    var2=var2+1
#    print("your attempt number-",var2)
    if var1>18:
        var2=var2+1
        print("number greater")
        print("your attempt number",var2)
    if(var2>=9):
        print("GAME OVER")
        break
        continue

    if var1<18:
        var2=var2+1
        print("number smaller")
        print("your attempt number", var2)
    if (var2>=9):
        print("GAME OVER")
        break
        continue
    if var1==18:
        var2=var2+1
        print("congo you entered the correct number")
        print("your attempt number", var2)
    if (var2>=9):
        print("GAME OVER")
        break
        continue
