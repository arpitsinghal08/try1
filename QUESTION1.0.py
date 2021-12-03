#question- create a dictionary and take input from the user
# and return the meaning of the word from the dictionary
"""
d1={"mitigate":"to become less severe "
    ,"slated":"scheduled",
    "leverage":"power to influence",
    "allege":"claiming without proof"}
print("enter any word among MITIGATE,LEVERAGE,SLATED,ALLEGE")
inp=input()
print("you entered=",inp.upper()," \n\n  ")


print("the meaning of the word you entered is=",d1[inp].upper())
"""
d={"mitigate":"to become less severe "
    ,"slated":"scheduled",
    "leverage":"power to influence",
    "allege":"claiming without proof"}
print("enter you word")
var1=input()
print("meaning of your word--",d[var1])