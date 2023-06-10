import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('books.xlsx')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df['年份']
height=df['销售额']
plt.grid(axis="y", which="major")  # 生成虚线网格
#x、y轴标签
plt.xlabel('年份')
plt.ylabel('线上销售额（元）')
#图表标题
plt.title('2013-2019年线上图书销售额分析图')
plt.bar(x,height,width = 0.5,align='center',color = 'b',alpha=0.5,bottom=0.8)
#设置每个柱子的文本标签,format(b,',')格式化销售额为千位分隔符格式
for a,b in zip(x,height):
    plt.text(a, b,format(b,','), ha='center', va= 'bottom',fontsize=9,color = 'b',alpha=0.9)
#图例
plt.legend(['销售额'])

