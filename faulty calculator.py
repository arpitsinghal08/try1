print("enter you 1st number")
var1=input()
print("enter your 2nd number")
var2=input()
print("select operation among addition, multiplication, substraction,division")
var3=input()
var4=int(var1)+int(var2)
var5=int(var1)-int(var2)
var6=int(var1)*int(var2)
var7=int(var1)/int(var2)
if var1=="45" and var2=="3" and var3=="*":
    print("555")
elif var1=="56" and var2=="9" and var3=="+":
    print("77")
elif var1=="56" and var2=="6" and var3=="/":
    print("4")
elif var3=="+":
    print(var4)
elif var3=="-":
    print(var5)
elif var3=="*":
    print(var6)
elif var3=="/":
    print(var7)
