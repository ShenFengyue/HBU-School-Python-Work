import pandas as pd  #导入pandas模块
df=pd.read_csv('JD.csv',encoding='gbk')
#抽取数据
df1=df[['二级分类','7天点击量']]
df1=df1.groupby('二级分类')['7天点击量'].sum()
