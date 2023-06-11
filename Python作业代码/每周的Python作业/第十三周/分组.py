import pandas as pd
df = pd.read_excel("D:\\桌面\\Python\\每周Python作业\\第十三周\\data1.xlsx", header=None)
df1 = df[[6,7]]  # 选择第一列和第二列作为数据框的列
df1 = df1.groupby(6).sum()  # 按第一列进行分组并求和



