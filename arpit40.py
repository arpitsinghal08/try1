class employee:
    leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"my name is {self.name} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.leaves==new_leaves

    @classmethod
    def from_dash(cls,str):
        p=str.split("-")
        return cls(p[0],p[1],p[2])

    @staticmethod
    def printgood(string):
        print("this is good",string)
rohan=employee("rohan",455,"student")
sohan=employee.from_dash("sohan-444-instructor")






class programmer(employee):
    def __init__(self,name,salary,role,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages=languages
    leaves=55

    def printdetailsprogrammer(self):
        return f"my name is {self.name} and my" \
               f" role is {self.role} and my languages are{self.languages}"

shubham=programmer("shubham",800,"programmer",["python","java"])
karan=programmer("karan",900,"programmer",["python"])
pappu=employee("pappu",100,"teacher")


print(karan.printdetails())
print(karan.printdetailsprogrammer())
print(shubham.printdetailsprogrammer())

print(rohan.leaves)
print(shubham.leaves)

