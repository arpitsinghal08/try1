class employee:
    leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def getdetails(self):
        return f"name is {self.name} salary is" \
               f" {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.leaves=newleaves

    @classmethod
    def from_str(cls,string):
        pass


rohan=employee("rohan",455,"student")
sohan=employee("sohan",555,"instructor")

rohan.change_leaves(44)
print(sohan.leaves)
print(rohan.leaves)
