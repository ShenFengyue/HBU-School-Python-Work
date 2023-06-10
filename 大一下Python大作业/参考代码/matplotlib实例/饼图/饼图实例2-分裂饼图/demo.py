import pandas as pd
from matplotlib import pyplot as plt
df1 = pd.read_excel('data2.xls')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.figure(figsize=(5,3)) #设置画布大小
labels = df1['地区']
sizes = df1['销量']
#设置饼形图每块的颜色
colors = ['red', 'yellow', 'slateblue', 'green','magenta','cyan','darkorange','lawngreen','pink','gold']
plt.pie(sizes, #绘图数据
        labels=labels,#添加区域水平标签
        colors=colors,# 设置饼图的自定义填充色
        labeldistance=1.02,#设置各扇形标签（图例）与圆心的距离
        autopct='%.1f%%',# 设置百分比的格式，这里保留一位小数
        startangle=90,# 设置饼图的初始角度
        radius = 0.5, # 设置饼图的半径
        center = (0.2,0.2), # 设置饼图的原点
        textprops = {'fontsize':9, 'color':'k'}, # 设置文本标签的属性值
        pctdistance=0.6,# 设置百分比标签与圆心的距离
        #shadow=True,      #阴影
        explode = (0.1,0,0,0,0,0,0,0,0,0))  #设置分裂饼图
        #explode = (0.1,0,0,0,0,0,0,0.1,0.1,0))  #设置多分裂饼图
# 设置x，y轴刻度一致，保证饼图为圆形

plt.axis('equal')
plt.title('2020年1月各地区销量占比情况分析')
