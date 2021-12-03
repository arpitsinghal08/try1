class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname


    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    def email(self):
        return f"{self.lname}{self.fname}@class.com"


rohan_garg= employee("rohan","garg")
print(rohan_garg.email())
# rohan_garg.fname="sohan"
# print(rohan_garg.email())
print(type(rohan_garg))
print(id(rohan_garg))
print(dir(rohan_garg))
