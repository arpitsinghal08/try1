def gettime():
    import datetime
    return datetime.datetime.now()
# print("")


def function():
    print("choose your client")
    client=int(input("1.ram\n2.rohan\n3.sohan"))
    if client==1:
        print("what do you want fo ram")
        choice=int(input("1.diet\n2.exercise"))
        if choice==1:
            f=open("ramdiet","a")
            var1=input("what did ram ate?")
            f.write(str([str(gettime())]) + " "+ var1)
            print("successfully updated")
            f.close()
        if choice==2:
            f=open("ramdiet","a")
            var1=input("which exercise?")
            f.write(str([str(gettime())]) +" "+ var1)
            print("successfullly updated")
            f.close()

def function2():
    print("choose client")
    client=int(input("1.ram\n2.rohan\n3.sohan"))
    if client==1:
        print("what do you want to retrieve for ram")
        choice=int(input("1.diet\n2.exercise"))
        if choice==1:
            f=open("ramdiet")
            print(f.readlines())
            f.close()


print("welcome to health management system")
option = int(input("1.add data\n\n2.retrieve"))
if option==1:
        function()
elif option==2:
        function2()
else:
        print("wrong input try again")

