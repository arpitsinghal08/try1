#011235813   next number appears
# after adding previous 2 numbers
#print function for nth fibbonaci number

def fiboo(n):
    if n==1 or n==0:
        return 0
    if n==2:
        return 1
    if n<0:
        return print("incorrect input")

    else:
        return fiboo(n-1)+fiboo(n-2)
var1=int(input("enter nth number you want to be printed."))
print(fiboo(var1))


