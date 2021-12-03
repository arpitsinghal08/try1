#45*3=77 ,56/6=6, 56-6=60
print("enter your first number")
var1= int(input())
print("enter your second number")
var2=int(input())
print("choose operation(*,+,-,/,)")
var3=input()
var4=int(var1)+int(var2)
var5=int(var1)/int(var2)
var6=int(var1)-int(var2)
var7=int(var1)*int(var2)
if var1==45 and var2==3 and var3=="*":
    print("77")
elif var1==56 and var2==6 and var3=="/":
    print("6")
elif var1==56 and var2==6 and var3=="-":
    print("60")
elif var3=="+":
    print(var4)
elif var3=="/":
    print(var5)
elif var3=="*":
    print(var7)
elif var3=="-":
    print(var6)


