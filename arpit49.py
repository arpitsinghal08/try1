#generator
#iterable - object on which __iter__() or
# __getitem__() is defined

#iterator-__next__()
# iteration- process of iterate

#generator-
#
# def gen(n):
#     for i in range(0,n):
#         yield i
#
# g=gen(4)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())

# var1="arpit"
# for item in var1:
#     print(item)

var1="arpit"
a=iter(var1)
print(a.__next__())
