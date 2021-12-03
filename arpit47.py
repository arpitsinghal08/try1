#    ABSTRACT BASE CLASS
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass


class rectangle(shape):
    type="rectangle"
    sides=4
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
var1=int(input("enter length\n"))
var2=int(input("enter breadth\n"))
rect1=rectangle(var1,var2)
print(rect1.area())