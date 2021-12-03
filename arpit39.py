class employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    @classmethod
    def fromstring(cls,string):
        p=string.split("-")
        return cls(p[0],p[1],p[2])
    @staticmethod
    def function(string):
        print(f"{string},this is {rohan.name},my role is {rohan.role}")



rohan=employee.fromstring("rohan-455-student")

employee.function("hello")
