import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
df1 = pd.read_excel('data2.xls')
df2=pd.read_excel('data2.xls',sheet_name='2月')
#数据集，x1,x2分别对应外环、内环百分比例
x1=df1['销量']
x2=df2['销量']
#设置饼状图各个区块的颜色
colors = ['red', 'yellow', 'slateblue', 'green','magenta','cyan','darkorange','lawngreen','pink','gold']
#外环
plt.pie(x1,autopct='%.1f%%',radius=1,pctdistance=0.85,colors=colors,wedgeprops=dict(linewidth=2,width=0.3,edgecolor='w'))
#内环
plt.pie(x2,autopct='%.1f%%',radius=0.7,pctdistance=0.7,colors=colors,wedgeprops=dict(linewidth=2,width=0.4,edgecolor='w'))
#图例
legend_text=df1['地区']
plt.legend(legend_text,title='地区',frameon=False,bbox_to_anchor=(0.2,0.5))#设置图例标题、位置、去掉图例边框
plt.axis('equal')#设置坐标轴比例以显示为圆形
plt.title('2020年1月和2月各地区销量占比情况分析')
