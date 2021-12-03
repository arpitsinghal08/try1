#operator overloading and dunder method

class employee:
    leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):
        return f"the name is {self.name} and salary is {self.salary}"

    # def __add__(self, other):
    #     return self.salary+other.salary
    # def __truediv__(self, other):
    #     return self.salary/other.salary



    def __repr__(self):
        return f"employee({self.name},{self.salary})"



    def __str__(self):
        return f"my name is {self.name} and my salary is {self.salary}"
rohan=employee("rohan",455,"programmer")
sohan=employee("sohan",500,"coder")
print(rohan)
print(repr(rohan))





# print(rohan.salary+sohan.salary)
# print(rohan+sohan)
# print(rohan/sohan)

