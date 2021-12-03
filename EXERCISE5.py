#HEALTH MANAGEMENT SYSTEM
 #3 CLIENTS-ROHAN,SOHAN ,MOHAN
 # DIET AND EXERCISE
  # TOTAL 6 FILES
  # 3 DIET 3EXERCISE
  # WRITE A FUNCTION WHEN EXECUTED TAKE AS INPUT CLIENT NAME AND ASKS DIET OR EXERCISE AND PRINT REQUIRED INFORMATION
print("enter client name")
var1=str(input())
if var1==str("rohan"):
    print("for diet type 1 and for exercise type0")
    var2=int(input())
    boolean=bool(var2)
    if boolean==True:
        f=open("ROHANDIET")
        content=f.read()
        print(content)
        f.close()
    if boolean == False:
        f = open("ROHANEXERCISE")
        content = f.read()
        print(content)
        f.close()
if var1==str("sohan"):
    print("for diet type 1 and for exercise type0")
    var2=int(input())
    boolean=bool(var2)
    if boolean==True:
        f=open("SOHANDIETDIET")
        content=f.read()
        print(content)
        f.close()
    if boolean == False:
        f = open("SOHANDIETEXERCISE")
        content = f.read()
        print(content)
        f.close()

if var1==str("mohan"):
    print("for diet type 1 and for exercise type0")
    var2=int(input())
    boolean=bool(var2)
    if boolean==True:
        f=open("MOHANDIET")
        content=f.read()
        print(content)
        f.close()
    if boolean == False:
        f = open("MOHANEXERCISE")
        content = f.read()
        print(content)
        f.close()