#write a program in which people
# have to guess the number[18] and you have to guide
# the person to reach tha correct number by telling that
# the number entered is greater or smaller
# maximum number of guesses=9
#print number of guesses left
#after 9 guesses print game over
#number of guesses used


while(1):
    print("enter your number")
    var1=int(input())
    if var1>20:
        print("entered number is greater")
        continue
    if 20>var1>18:
        print("entered numbered is greater but very close")
        continue
    if 15<var1<18:
        print("entered number is smaller but very close")
        continue
    if var1<15:
        print("entered numbered is smaller")
        continue
    if var1==18:
        print("you entered correct number and game over")
        break