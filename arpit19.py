# f=open("arpit.txt")
# print(f.readline())
# print(f.readlines())
# f.close()

with open("arpit.txt") as f:
    a=f.read()
    print(a)

p=open("arpit.txt")
content=p.read()
print(content)
p.close()

