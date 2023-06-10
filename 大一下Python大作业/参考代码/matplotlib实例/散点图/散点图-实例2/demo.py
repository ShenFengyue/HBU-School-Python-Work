import pandas as pd
import matplotlib.pyplot as plt
aa =r'JDdata.xls'
bb=r'JDcar.xls'
dfaa = pd.DataFrame(pd.read_excel(aa))
dfbb=pd.DataFrame(pd.read_excel(bb))
df1=dfaa[['业务日期','金额']]
df2=dfbb[['投放日期','支出']]
#去除空日期和金额为0的记录
df1=df1[df1['业务日期'].notnull() & df1['金额'] !=0]
df2=df2[df2['投放日期'].notnull() & df2['支出'] !=0]
df1['业务日期'] = pd.to_datetime(df1['业务日期'])
df2['投放日期'] = pd.to_datetime(df2['投放日期'])
dfData = df1.set_index('业务日期',drop=True)
dfCar=df2.set_index('投放日期',drop=True)
# 按月度统计并显示销售金额
dfData_month=dfData.resample('M').sum().to_period('M')
# 按月度统计并显示广告费支出金额
dfCar_month=dfCar.resample('M').sum().to_period('M')
#x为广告费用，y为销售收入
x=pd.DataFrame(dfCar_month['支出'])
y=pd.DataFrame(dfData_month['金额'])
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.title('销售收入与广告费散点图')   #图表标题
plt.scatter(x, y,  color='red') #真实值散点图





