import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df=pd.read_excel('体温.xls')               #导入Excel文件
#折线图
x=df['日期']                  #x轴数据
y=df['体温']                  #y轴数据
plt.plot(x,y,color='m',linestyle='-',marker='o',mfc='w')
plt.xlabel('2020年2月')        #x轴标题
plt.ylabel('基础体温')         #y轴标题




