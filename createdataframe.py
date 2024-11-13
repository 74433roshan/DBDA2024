import numpy as np
import pandas as pd
#create simple dataframe
np.random.seed(102)
mydata=np.random.randint(0,100,(4,3))
print(mydata)
myindex=['CA','NY','YX','AZ']
mycolumn=['Jan','Feb','Mar']

df=pd.DataFrame(data=mydata)
print(df)

df=pd.DataFrame(data=mydata,index=myindex)
print(df)

df=pd.DataFrame(data=mydata,index=myindex,columns=mycolumn)
print(df)
