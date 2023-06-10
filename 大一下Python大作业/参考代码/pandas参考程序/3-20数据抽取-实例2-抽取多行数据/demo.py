import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
df1=df.loc[['明日','高袁圆']]  #抽取任意多行数据
df2=df.iloc[[0,2]]    #抽取任意多行数据