import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# 设置中文字体
font_path = 'C:\Windows\Fonts\SimHei.TTF'  # 替换为中文字体文件的路径
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 从 Excel 文件读取数据
df = pd.read_excel('D:\桌面\Python大作业\data.xlsx', usecols=['10、您对短视频对依赖程度'])
data = df['10、您对短视频对依赖程度'].tolist()

# 统计不同依赖程度的人数
count_dict = {}
for value in data:
    if value in count_dict:
        count_dict[value] += 1
    else:
        count_dict[value] = 1

# 提取不同依赖程度和对应人数
x = list(count_dict.keys())
y = list(count_dict.values())

# 绘制柱形图
plt.bar(x, y)
plt.xlabel('依赖程度')
plt.ylabel('人数')
plt.title('不同依赖程度的人数统计')

plt.show()
