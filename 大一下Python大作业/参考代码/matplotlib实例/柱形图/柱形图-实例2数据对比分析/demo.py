import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('books.xlsx',sheet_name='Sheet2')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df['年份']
y1=df['京东']
y2=df['天猫']
y3=df['自营']
width =0.25  #柱子宽度，若显示n个柱子，则width值需小于1/n ，否则柱子会出现重叠
#y轴标签
plt.ylabel('线上销售额（元）')
#图表标题
plt.title('2013-2019年线上图书销售额分析图')
plt.bar(x,y1,width = width,color = 'darkorange')
plt.bar(x+width,y2,width = width,color = 'deepskyblue')
plt.bar(x+2*width,y3,width = width,color = 'g')
#设置每个柱子的文本标签,format(b,',')格式化销售额为千位分隔符格式
for a,b in zip(x,y1):
    plt.text(a, b,format(b,','), ha='center', va= 'bottom',fontsize=8)
for a,b in zip(x,y2):
    plt.text(a+width, b,format(b,','), ha='center', va= 'bottom',fontsize=8)
for a, b in zip(x, y3):
    plt.text(a + 2*width, b, format(b, ','), ha='center', va='bottom', fontsize=8)
plt.legend(['京东','天猫','自营'])#图例
