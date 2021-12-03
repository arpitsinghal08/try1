#DECORATORS
# def function1():
#     print("hello")
# func2=function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# print(funcret(0))


def decorator(function):

    def nowexec():

        print("executing now")

        function()

        print("executed")

    return nowexec

@decorator

def arpit():
    print("arpit is a good boy")
arpit()
