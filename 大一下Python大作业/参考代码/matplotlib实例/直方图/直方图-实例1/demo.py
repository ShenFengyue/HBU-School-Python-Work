import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('grade1.xls')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df['得分']
plt.xlabel('分数')
plt.ylabel('学生数量')
# 显示图标题
plt.title("高一数学成绩分布直方图")
plt.hist(x, bins = [0,25,50,75,100,125,150],facecolor="blue", edgecolor="black", alpha=0.7)
