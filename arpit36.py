"""
class Employee:
    leaves=8
    def priintdetails(self):
        return f"name is {self.name} salary is {self.salary} and role is {self.role}"
rohan=Employee()
sohan=Employee()
rohan.name="rohan"
rohan.salary=455
sohan.salary=555
rohan.role="instructor"
sohan.role="student"
sohan.name="sohan"
print(rohan.priintdetails())
print(rohan.leaves)
"""
               # constructor

class employee:
    leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def getdetails(self):
        return f"name is {self.name} salary is {self.salary} and role is {self.role}"
rohan=employee("rohan",455,"student")
print(rohan.getdetails())

