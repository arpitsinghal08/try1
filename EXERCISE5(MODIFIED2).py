#HEALTH MANAGEMENT SYSTEM
print("press 1 to lock or press 0 to retrieve")
var1=int(input())
boolean=bool(var1)
if boolean==True:
    print("press 1 for ram 2 for mohan 3 for rohan")
    var2=int(input())
    if var2==1:
        print("press 1 for diet and 0 for exercise")
        var3=input()
        bol=bool(var3)
        if bol==True:
            f = open("ramdiet", "a")
            print("write here about your meals")
            var4 = str(input())
            f.write(var4)
            f.close()


        if bol==False:
            f = open("ramexercise","a")
            print("write here about your exercise")
            var5 =str(input())
            f.write(var5)
            f.close()



if boolean==False:
    print("press 1 for ram 2 for mohan 3 for rohan")
    var6=input()
    if var6==1:
        print("press 1 for diet and 0 for exercise")
        var7 = input()
        bol=bool(var7)
        if bol==True:
            def getdate():
                import datetime


                return datetime.datetime.now()








# def getdate():
    # import datetime
    # return datetime.datetime.now()