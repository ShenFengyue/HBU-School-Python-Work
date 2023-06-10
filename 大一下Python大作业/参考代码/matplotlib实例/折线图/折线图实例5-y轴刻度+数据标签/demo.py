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

#设置x轴刻度及标签
dates=['1日','2日','3日','4日','5日',
       '6日','7日','8日','9日','10日',
       '11日','12日','13日','14日']
plt.xticks(range(1,15,1),dates)
plt.yticks([35.4,35.6,35.8,36,36.2,36.4,36.6,36.8,
            37,37.2,37.4,37.6,37.8,38])
for a,b in zip(x,y):
    plt.text(a,b+0.05,'%.1f'%b,ha = 'center',va = 'bottom',fontsize=9)
