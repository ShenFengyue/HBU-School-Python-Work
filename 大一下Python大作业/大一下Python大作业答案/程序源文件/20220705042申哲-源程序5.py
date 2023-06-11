import pandas as pd
from matplotlib import pyplot as plt
import os

current_directory = os.getcwd()
print(current_directory)

df1 = pd.read_excel('D:\桌面\Python大作业\data.xlsx')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.figure(figsize=(5,3)) #设置画布大小

grouped = df1.groupby('12、短视频对您的价值观塑造是否有影响')
labels = grouped['12、短视频对您的价值观塑造是否有影响'].first().tolist()
sizes = grouped['7、您每天使用短视频的时间是多久'].sum().tolist()

#设置饼形图每块的颜色
colors = ['red', 'yellow']
plt.pie(sizes, #绘图数据
        labels=labels,#添加区域水平标签
        colors=colors,# 设置饼图的自定义填充色
        labeldistance=1.02,#设置各扇形标签（图例）与圆心的距离
        autopct='%.1f%%',# 设置百分比的格式，这里保留一位小数
        startangle=90,# 设置饼图的初始角度
        radius = 0.5, # 设置饼图的半径
        center = (0.2,0.2), # 设置饼图的原点
        textprops = {'fontsize':9, 'color':'k'}, # 设置文本标签的属性值
        pctdistance=0.6)# 设置百分比标签与圆心的距离

plt.axis('equal')    # 设置x，y轴刻度一致，保证饼图为圆形
plt.title('手机使用时间与是否对价值观造成影响的关系\n（面积表示刷短视频的时间总和）')
plt.show()
