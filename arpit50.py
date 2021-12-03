#comprehension

#       LIST COMPREHENSION
# list=[]
# for i in range (0,100):
#     if i%3==0:
#         list.append(i)
#
# print(list)

# list=[i for i in range(0,100) if i%3==0]
# print(list)


#    DICTIONARY COMPREHENSION

# dict1={0:"item1",1:"item2"}

# dict1={i:f"item{i}" for i in range(1,100) if i%10==0 }
# dict1={i:f"item{i}" for i in range(1,100)}
# dict2={value:key for key,value in dict1.items()}
# print(dict1)
# print(dict2)

 #       GEENRATOR COMPREHENSION

evens=(i for i in range (0,100) if i%2==0)
print((evens))
print(evens.__next__())
print(evens.__next__())