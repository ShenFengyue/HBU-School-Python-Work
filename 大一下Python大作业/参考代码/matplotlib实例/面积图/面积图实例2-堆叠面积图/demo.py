import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('books.xlsx',sheet_name='Sheet2')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df['年份']
y1=df['京东']
y2=df['天猫']
y3=df['自营']
#图表标题
plt.title('2013-2019年线上图书销售情况')
plt.stackplot(x, y1,y2,y3,colors=['#6d904f','#fc4f30','#008fd5'])
#图例
plt.legend(['京东','天猫','自营'],loc='upper left')
