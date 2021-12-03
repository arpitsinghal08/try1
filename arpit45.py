# polymorphism
class A:
    classvar1="i am a class variable in class a"
    def __init__(self):
        self.var1="i am inside class a"
        self.classvar1="instance var in class a"
        self.special="special"


class B(A):
    classvar1 = "in am in class b"
    def __init__(self):
        self.var1="i am inside class b"
        self.classvar1="instance var in class b"



a=A()
b=B()
print(b.var1)
print(b.classvar1)
print(b.speacial)