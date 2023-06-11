import pandas as pd

# 读取Data1.xlsx和Data2.xlsx的数据
data1 = pd.read_excel('D:\桌面\Python\每周Python作业\第十三周\data1.xlsx')
data2 = pd.read_excel('D:\桌面\Python\每周Python作业\第十三周\data2.xlsx')

# 合并两个表格
merged_data = pd.concat([data1, data2], ignore_index=True)

# 保存合并后的表格为新的Excel文件
merged_data.to_excel('MergedData.xlsx', index=False)



