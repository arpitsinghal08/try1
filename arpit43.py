class dad:
    basketball=1

class son(dad):
    dance=1
    basketball=9
    def isdance(self):
        return f"yes i dance  and i know {self.dance} forms"

class grandson(son):
    dance=6
    def isdance(self):
        return f"yes i dance  and i know {self.dance} forms"


darry=dad()
larry=son()
harry=grandson()
print(larry.isdance())
print(harry.isdance())
print(harry.basketball)


    







