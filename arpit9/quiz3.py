#make a list having anything in it but
# rint only those things which are greater than 6
# and are numbers
list=["arpit",3,7,6,8,2,"ram","mohan"]
for item in list:
    if  str(item).isnumeric() and str(item)>str(6):
        print(item)



#PRACTICE
list2=[1,3,4,5,6,7,"apit ","ram"]
for item in list2:
    if str(item).isnumeric() and str(item)>str(6):
        print(item)