#PUBLIC,PRIVATE AND PROTECTED ACEESS SPECIFIERS
# PUBLIC-SHARE WITH EVERYONE(EVERYONE IN NEIGHBOURHOOD)
# PRIVATE-ONLY YOU
# PROTECTED-GHARWALE(FAMILY MEMBER)

# class employee:
#     leaves=8
#     __number_of_employee=90
#     def __init__(self,name,salary,role):
#         self.name=name
#         self.salary=salary
#         self.role=role
#     def printdetails(self):
#         return f"name is {self.name} and role is {self.role}"
#
# rohan=employee("rohan",400,"student")
# print(rohan._employee__number_of_employee)
#
# class player(employee):
#     pass
#
#     def __init__(self,name,game):
#         self.name=name
#         self.game=game
#
# shubham=player("shubham","cricket")
#
# print(shubham._employee__number_of_employee)






# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary


# rohan=employee("rohan",600)
# # print(rohan._employee__salary)
#

# class player(employee):
#     pass
#     # def __init__(self,name,salary,game):
#     #     self.name=name
#     #     self.game=game
# shubham=player("shubham",45)
# print(shubham.salary)


# class employee:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
#
#
# rohan=employee("rohan",777)
# print(rohan._employee__salary)




# class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def function33(self):
#         return f"name {self.name} and age {self.age}"
#
# rohan=employee("rohan",23)
#
# print(rohan.age)
# print(rohan.function33())

# class employee:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def _function33(self):
#         return f"name {self._name} and age {self._age}"
#
# rohan=employee("rohan",23)
#
# print(rohan._age)
# print(rohan._function33())
#
#
# class player(employee):
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#
#     def details(self):
#         return f"name {self._name} and age {self._age}"
# sohan=player("sohan",45)
#
# print(sohan._function33())

# program to illustrate access modifiers of a class

# super class

# class Super:
#     # public data member
#
#     var1 = None
#
#     # protected data member
#
#     _var2 = None
#
#     # private data member
#
#     __var3 = None
#
#     # constructor
#
#     def _init_(self, var1, var2, var3):
#         self.var1 = var1
#
#         self._var2 = var2
#
#         self.__var3 = var3
#
#     # public member function
#
#     def displayPublicMembers(self):
#         # accessing public data members
#
#         print("Public Data Member: ", self.var1)
#
#     # protected member function
#
#     def _displayProtectedMembers(self):
#         # accessing protected data members
#
#         print("Protected Data Member: ", self._var2)
#
#     # private member function
#
#     def __displayPrivateMembers(self):
#         # accessing private data members
#
#         print("Private Data Member: ", self.__var3)
#
#     # public member function
#
#     def accessPrivateMembers(self):
#         # accessing private member function
#
#         self.__displayPrivateMembers()
#
#
# # derived class
#
# class Sub(Super):
#
#     # constructor
#
#     def _init_(self, var1, var2, var3):
#         Super._init_(self, var1, var2, var3)
#
#     # public member function
#
#     def accessProtectedMembers(self):
#         # accessing protected member functions of super class
#
#         self._displayProtectedMembers()
#
#
# # creating objects of the derived class
#
# obj = Sub("Geeks", 4, "Geeks !")
#
# # calling public member functions of the class
# obj.displayPublicMembers()
# obj.accessProtectedMembers()
# obj.accessPrivateMembers()
#
# # Object can access protected member
#
# print("Object is accessing protected member:", obj._var2)
#
# # object can not access private member, so it will generate Attribute error
# # print(obj.__var3)



class employee:
    leaves=8
    __number_of_employee=90
    def __init__(self,name,salary,role):
        self._name=name
        self._salary=salary
        self._role=role
    def printdetails(self):
        return f"name is {self.name} and role is {self.role}"

rohan=employee("rohan",400,"student")

class player(employee):
    pass

    def __init__(self,name,game):
        self.name=name
        self.game=game

shubham=player("shubham","cricket")

print(shubham._employee__number_of_employee)