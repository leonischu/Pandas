import pandas as pd;
# var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
# print(var)
# var["C"]=var["A"]+var["B"]
# var["C"]=var["A"]*var["B"]
# var["C"]=var["A"]/var["B"]

# print(var)


var=pd.DataFrame({"A":[10,20,30,40],"B":[50,60,70,80]})

var["Python"]  =var["A"]<20
var["Python_1"]  =var["B"]>=60

print(var)