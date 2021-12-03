#args and kwargs
# def function(a,b,c,d):
#     print(a,b,c,d)
# function("arpit","ram","sohan","sohan")

# def args(*args):
#     for item in args:
#         print(item)
#     print(args)
#
# var1=["arpit","ram","sohan","rohan"]
# args(*var1)

#
# def args(*args):
#     print(args)
#
# normal="hello"
# var=["arpit","ram","sohan","sohan"]
# args(normal,*var)



def function(normal,*args,**kwargs):
    for item in args:
        print(item)
    for items in kwargs.items():
        print(items)
var1=["arpit","ram","sohan","sohan"]
normal="hello"
kw={"arpit":"1","ram":"2","rohan":"3"}
function(normal,*var1,**kw)

