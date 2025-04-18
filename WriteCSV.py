import pandas as pd;
dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}
d = pd.DataFrame(dis)
print(d)
# create a csv file
# d.to_csv("Test_new.csv",index=False)
d.to_csv("Test_new.csv",index=False,header=[1,2,3])