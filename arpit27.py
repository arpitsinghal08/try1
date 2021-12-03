# enumerate function(helps in
# making programming easy)

list=["bhindi","aloo","chopsticks","noodles"]
# i=1
# for item in list:
#     if i%2 is not 0:
#         print(f"please buy {item}")
#     i+=1


for index,item in enumerate(list):
    if index%2==0:
        print(f"please buy {item}")

