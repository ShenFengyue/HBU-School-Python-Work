import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#抽取指定列数据——使用loc方法和iloc方法
print(df.loc[:,['语文','数学']])   #抽取“语文”和“数学”
print(df.iloc[:,[0,1]])            #抽取第1列和第2列
print(df.loc[:,'语文':])           #抽取从“语文”开始到最后一列
print(df.iloc[:,:2])               #连续抽取从1列开始到第3列
