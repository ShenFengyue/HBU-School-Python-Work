import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('books.xlsx')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df['年份']
y=df['销售额']
#图表标题
plt.title('2013-2019年线上图书销售情况')
plt.stackplot(x, y)
