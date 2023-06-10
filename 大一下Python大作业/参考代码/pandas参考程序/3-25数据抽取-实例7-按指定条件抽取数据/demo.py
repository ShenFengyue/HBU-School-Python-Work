import pandas as pd

data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#按指定条件抽取数据，基于位置的查询iloc[],基于行名、列明的查询
df1=df.loc[(df['语文'] > 105) & (df['数学'] >88)]
