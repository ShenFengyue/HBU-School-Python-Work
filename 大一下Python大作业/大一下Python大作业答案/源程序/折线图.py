import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 加载数据
df = pd.read_excel(r'D:\桌面\Python大作业\data.xlsx')

# 删除每天刷短视频超过12小时的数据
df = df[df['7、您每天使用短视频的时间是多久'] <= 12]

# 按照年级分组并求平均值
grouped = df.groupby('2、您的年级是：')['7、您每天使用短视频的时间是多久'].mean()

# 取前四个年级和对应的平均值
x = ['大一', '大二', '大三', '大四']
y = grouped.values[:4]

# 设置中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 绘制折线图
plt.plot(x, y, marker='o')

# 设置图表标题和轴标签
plt.title('不同年级每日刷短视频时间变化')
plt.xlabel('年级')
plt.ylabel('每日刷短视频时间（小时）')

# 显示图表
plt.show()
