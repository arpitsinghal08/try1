#try expect
"""
print("enter 1st number")
try:
    num1 = int(input())
except Exception as r:
    print(r)
print("enter 2nd number")
num2=int(input())
try:
    print("sum-",num1+num2)
except Exception as e:
    print(e)

print("this is a very important line")

"""
print("enter 1st number")
num1=input()
try:
    print(int(num1)*10)
except Exception as e:
    print(e)
