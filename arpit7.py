s=set()
print(type(s))
s1=set([1,2,3,4,5])
print(s1)
print(type(s1))
s.add(1)
s.add(1)
s.add(2)
s2=s.union({1,2,3})
print(s)
print(s2)
s3=s.intersection({1,2,3})
print(s3)
print(s.isdisjoint(s3))
s4=set([5,6,7])
print(s4.isdisjoint(s)
s.remove(2)
print(s)






