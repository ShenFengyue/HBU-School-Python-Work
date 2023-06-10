import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
df1=df.loc['明日'] #以列明和行名作为参数
print(df1)
df2=df.iloc[0]   #以行和列的位置索引作为参数
