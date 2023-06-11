import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('D:\\桌面\\Python\\每周Python作业\\第十三周\\data1.xlsx',header=None)

# 根据性别进行分组计数
grouped = df.groupby('gender').sum()

# 打印分组计数结果
print(grouped)
