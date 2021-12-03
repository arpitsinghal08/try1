class Employee:
    leaves=8
    pass

rohan=Employee()
sohan=Employee()
rohan.name="rohan"
rohan.salary=455
sohan.salary=555
rohan.role="instructor"
sohan.role="student"
sohan.name="sohan"
print(rohan.__dict__)
print(rohan.leaves)
print(Employee.leaves)
Employee.leaves=9
print(Employee.leaves)
print(rohan.leaves)
rohan.leaves=10
print(rohan.leaves)
print(Employee.leaves)
print(rohan.__dict__)
