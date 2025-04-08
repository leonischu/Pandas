import pandas as pd
x=[3,4,5,6]
var=pd.Series(x,index=['a','s','d','m'],dtype="float" ,name='python')
print(var)
print(type(var))
print(var[2])

# using dict
dic ={"name":['python','c','c++','java'],"por":[12,13,14,15],"rank":[1,2,3,4]}
var1=pd.Series(dic)
print(var1)

#single data
s=pd.Series(12,index=[1,2,3,4,5,6,7])
print(s)
print(type(s))

#No Broadcast error
s1=pd.Series(12,index=[1,2,3,4,5,6,7])
s2=pd.Series(12,index=[1,2,3,4])
print(s1+s2)
