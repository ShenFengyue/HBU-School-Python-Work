import pandas as pd  #导入pandas模块
df=pd.read_csv('JD.csv',encoding='gbk')
#抽取数据
df1=df[['一级分类','二级分类','7天点击量','订单预定']]
df2=df1.groupby(['一级分类','二级分类']).sum()    #分组统计求和
