import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#抽取指定行列数据
print(df.loc['七月流火','英语'])              #“英语”成绩
print(df.loc[['七月流火'],['英语']])          #“七月流火”的“英语”成绩
print(df.loc[['七月流火'],['数学','英语']])   #“七月流火”的“数学”和“英语”成绩
print(df.iloc[[1],[2]])                       #第2行第3列
print(df.iloc[1:,[2]])                        #第2行到最后一行的第3列
print(df.iloc[1:,[0,2]])                      #第2行到最后一行的第1列和第3列
print(df.iloc[:,2])                           #所有行，第3列




