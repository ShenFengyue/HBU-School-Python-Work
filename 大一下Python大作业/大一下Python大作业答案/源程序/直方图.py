import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'D:\桌面\Python大作业\data.xlsx')

# 过滤掉每天刷短视频时间大于12小时的数据
filtered_female_data = df.loc[(df['1、您的性别：'] == '女') & (df['7、您每天使用短视频的时间是多久'] <= 12), '7、您每天使用短视频的时间是多久']
filtered_male_data = df.loc[(df['1、您的性别：'] == '男') & (df['7、您每天使用短视频的时间是多久'] <= 12), '7、您每天使用短视频的时间是多久']

average_female = filtered_female_data.mean()
average_male = filtered_male_data.mean()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(axis="y", which="major")

plt.xlabel('性别')
plt.ylabel('每日短视频使用时间（小时）')

plt.title('男生和女生每日短视频使用时间')

plt.bar('女生', average_female, color='r', alpha=0.5)
plt.bar('男生', average_male, color='g', alpha=0.5)

plt.text('女生', average_female, f'女生平均值: {average_female:.2f}小时', ha='center', va='bottom', color='r')
plt.text('男生', average_male, f'男生平均值: {average_male:.2f}小时', ha='center', va='bottom', color='g')

plt.show()
