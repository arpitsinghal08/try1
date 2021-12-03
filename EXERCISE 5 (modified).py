
# HEALTH MANGAHEMENT SYSTEM
# PROGRAM SHOULD ASK NAME OF CLIENT WHOSE DIET OR EXERCISE NEEDS TO BE LOCKED
# THEN SHOULD ASK ABOUT DIET OR EXERCISE
# THEN WHATEVER HE WRITES SHOULD BE LOCKED(WRITTEN) IN THIS TXT FILE


# def getdate():
    # import datetime
    # return datetime.datetime.now()

      # DONE MYSELF
print("enter clients name--")
var1=input()
if var1==("ram"):
    print("type 1 for diet and 0 for exercise")
    var2=int(input())
    boolean=bool(var2)
    if boolean==True:
        while(1):
            f = open("ramdiet", "a")
            print("enter your meal time")
            var3 = input()
            print("enter your meal")
            var4 = input()
            var5 = var3, var4
            f.write(str(var5))
            f.close()



