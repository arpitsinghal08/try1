#dictionay is key value pairs
"""
d1={}
print(type(d1))
d2={"arpit":"burger","minal":"pizza" ,"ram":"roti"}
print(d2)
print(d2["arpit"])
d3={"rohan":{"b":"oats","l":"roti","d":"milk"}}
print(d3["rohan"]["b"])
print(d3)
d2["ankit"]="rice"
d2["lakshman"]="fruits"
print(d2)
del d2["arpit"]
print(d2)
"""
d2={"arpit":"burger","minal":"pizza" ,"ram":"roti"}
d3={"ram":"rajma","shyam":"roti","laksham":{"breakfast":"oats","lunch":"maggie","dinner":"milk"}}
#print(d3)
"""
d4=d2.copy()
del d4["ram"]
print(d4)
print(d2)

"""
"""print(d2.get("arpit"))
print(d2["arpit"])
d2.update({"leena": "toffee"})
print(d2)"""
print(d2.keys())
print(d2.items())
