#45*3=77 56-6=90 56/6=6
print("enter your first number")
var1= input()
print("enter your second number")
var2=input()
print("choose operation(*,+,-,/,)")
var3=input()
var4=int(var1)+int(var2)
var5=int(var1)/int(var2)
var6=int(var1)-int(var2)
var7=int(var1)*int(var2)
if var3=="+":
    print(var4)
if var3=="-":
    print(var6)
if var3=="/":
    print(var5)
if var3=="*":
    print(var7)