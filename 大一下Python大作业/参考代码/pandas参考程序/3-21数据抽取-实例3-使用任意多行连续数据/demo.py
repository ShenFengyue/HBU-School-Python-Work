import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#抽取连续任意多行数据
print(df.loc['明日':'二月二']) #从“明日”到“二月二”
print(df.loc[:'七月流火'])     #第1行到“七月流火”
print(df.iloc[0:3])            #第1行到第4行
print(df.iloc[1::])            #第2行到最后1行

