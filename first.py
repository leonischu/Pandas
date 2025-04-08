import pandas as pd
x=[3,4,5,6]
var=pd.Series(x,index=['a','s','d','m'],dtype="float" ,name='python')
print(var)
print(type(var))
print(var[2])