"""
print("arpit")
print("minal")
print("arpit",end=" ")
print("minal")
print("arpit minal")
print( "arpit","\n","minal")
print("arpit","\t","minal")
var1="arpit singhal"
var2="34"
var3=34
var4=34.5
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(var1,var2)
print(var1+var2)
print(var1,var3)
print(var3,var4)
print(var3+var4)
print(var2,var3)
print(int(var2)+ var3)
print(10*"arpit\n")
print(10*"arpit\t")
print(10*("arpit minal\n"))
print("enter your number")
inp=input()
print("you entered=",inp)

mystr="arpit is a good boy"
print(mystr[0:45])
print(mystr[0:56:4])
print(type(mystr))
print(mystr.endswith("boy"))
print(mystr.upper())
print(mystr.count("a"))
print(mystr.find("a"))
print(mystr.capitalize())
print(mystr.isdecimal())
print(mystr.replace("is","a"))

grocery=("pulses","rice","chikpea"," soap")
print(type(grocery))
grocery1=["arpit","minal","ram","shyam"]
print(type(grocery1))
grocery2=("pulses rice chikpea soap")
print(grocery[1])
print(grocery1[1])
print(grocery2[1])

numbers=[1,2,3,7,4,6]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(89)
numbers.sort()
numbers.reverse()
print(numbers)
numbers.remove(7)
numbers.insert(2,43)
print(numbers)
numbers.pop()
print(numbers)
num=[1,2,5,3,7]
num[3]=67
print(num)

a=1
b=3
a,b=b,a
print(a)
"""
d1={"arpit":"pizza","minal":"burger","ram":"roti"}
"""
print(d1)
print(d1["arpit"])
d2={"arpit":{"morning":"oats","evening":"roti","dinner":"milk"}}
print(d2)
print(d2["arpit"]["morning"])
d1.update({"shyam":"rajma"})
print(d1)

print(d1.keys())
print(d1.items())

d1={"mitigate":"to become less severe","leverage":"power to influence","allege":"false claims"}
print("enter word among mitigate,leverage,allege")
var1=input()
print("you entered =",var1)
print("meaning of your word=",d1[var1])

#45*3=555,56+9=77,56/6=9
print("enter your first number")
var1=input()
print("enter your second number")
var2=input()
print("select operation")
var3=input()
var4= int(var1)+int(var2)
var5= int(var1)-int(var2)
var6= int(var1)*int(var2)
var7= int(var1)/int(var2)
if var1=="45" or "3" and var2=="45" or "3"and var3=="*":
    print("555")
elif var1=="56" and var2== "56 "and var3=="+":
    print("77")
elif var1=="56" and var2== "56" and var3=="/":
    print("6")
elif var3=="*":
    print(var6)
elif var3=="+":
    print(var4)
elif var3=="-":
    print(var5)
elif var3=="/":
    print(var7)
elif var3=="*":
    print(var6)

s=set()
print(type(s))
s1=set([1,2,3,4])
s1.add(5)
print(s1)
s2=s1.union({5,6,7,8})
print(s2)

list1=[1,2,3,4,5]
print(5 in list1)
if 5 in list1:
    print("yeah bro")
"""

