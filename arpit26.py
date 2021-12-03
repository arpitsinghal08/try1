#TIME MODULE
import time
# initial=time.time()
# # print(initial)
#
# k=0
# while(k<3):
#     print("arpit")
#     k=k+1
#
# print("while loop ran in",time.time()-initial)
#
#
# initial2=time.time()
# for i in range(0,3):
#     print("arpit")
#
# print("for loop ran in ",time.time()-initial2)


# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)


initial=time.time()
# print(initial)

k=0
while(k<3):
    print("arpit")
    k=k+1
    time.sleep(4)

print("while loop ran in",time.time()-initial)
time.sleep(4)

initial2=time.time()
for i in range(0,3):
    print("arpit")
time.sleep(4)
print("for loop ran in ",time.time()-initial2)
