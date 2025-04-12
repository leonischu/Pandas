import pandas as pd;
l=[1,2,3,4,5,6]
var =pd.DataFrame(l)
print(type(var))

dic={"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],"e":[1,2,3,4,5]}
# var1=pd.DataFrame(dic,columns=["a","e"],index=["a","e","s","f","g"])
var1=pd.DataFrame(dic)

print(type(var1))
print(var1)
print(var1["a"],[3])
