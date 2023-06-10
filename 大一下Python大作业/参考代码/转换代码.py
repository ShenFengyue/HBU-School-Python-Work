import pandas as pd

# 读取Excel文件
df = pd.read_excel('D:\桌面\Python\支高英大作业\Python大作业郭宇轩数据.xlsx')

# 将数据保存为文本文件，包含表头
df.to_csv('output.txt', sep='\t', index=False)
