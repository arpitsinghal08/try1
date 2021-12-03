"""library mangaer
create a library class
 display book
 lend book
 donate
 return

arpitlibrary=library(listofbooks,librray name)
dictionary for maintaining records
(name of book:person name)


create a main function and
run an infinite while loop

 """

print("welcome to ARPIT library")
class library:
    def __init__(self,listofbooks,library_name):
        self.listofbooks=listofbooks
        self.library_name=library_name

    def display(self):
