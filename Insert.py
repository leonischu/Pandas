import pandas as pd;
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5],"C":[11,12,13,14,15]})
print(var)
# var.insert(1,"Python",var["A"])
# print(var)
# var.insert(1,"Python_",[11,12,13,14,15])
# print(var)
# var['python']=var["A"][:3]
# print(var)

# DELETE
var1=var.pop("B")
print(var1)
print(var)
del var["A"]
print(var)