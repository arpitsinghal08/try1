#         SNAKE WATER GUN

import random


gamecounter=0

computer=0
player=0

# list=["snake","water","gun"]
# rand=random.choice(list)
s="snake"
w="water"
g="gun"
n=0
for n in range(0,5):
    var1 = input("choose snake, water or gun\n ")
    if var1 == s:
        list = ["water", "gun"]
        rand = random.choice(list)
        print("computer's choice--",rand)
        if rand == w:
            print("you won")
            player=player+1
            print("your score",player)
            print("computer score",computer)
            n = n + 1
            print("round number",n)
            continue

        else:
            print("computer won")
            computer+=1
            print("computer score",computer)
            print("your score",player)
            n=n+1
            print("round number",n)

            continue

    if var1 == w:

        list = ["snake", "gun"]
        rand = random.choice(list)
        print("computer's choice--",rand)
        if rand == g:
            print("you won")
            player+=1
            print("your score",player)
            print("computer score",computer)
            n = n + 1
            print("round number",n)

            continue
        else:
            print("computer won")
            computer+=1
            print("computer score",computer)
            print("your score",player)
            n=n+1
            print("round number",n)

            continue

    if var1 == g:
        list = ["water", "snake"]
        rand = random.choice(list)
        print("computer's choice--",rand)
        if rand == s:
            print("you won")
            player+=1
            print("your score",player)
            print("computer score",computer)
            n = n + 1
            print("round number",n)

            continue
        else:
            print("computer won")
            computer+=1
            print("computer score",computer)
            print("your score",player)
            n=n+1
            print("round number",n)

            continue

if player>computer:
    print("\ncongratulations YOU WON!")
if computer>player:
    print("\nHARD LUCK! computer won this time")
if computer==player:
    print("IT IS A TIE!")



# g=input("do you want to play again\n type YES or NO \n")
# y="yes"
# n="no"
# if g==n:
#     print("as you wish")
# else:
#     print("here you go again")









