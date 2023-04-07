#这是Python作业代码

import requests
import pandas as pd
import matplotlib.pyplot as plt

# 从问卷调查平台获取数据
response = requests.get('http://survey.example.com/data')
data = response.json()

# 将数据转化为DataFrame格式
df = pd.DataFrame(data)

# 对数据进行清洗和整理
df = df.drop_duplicates()   # 去重
df = df.dropna()            # 删除缺失值

# 数据分析
count_by_gender = df.groupby('gender').size()   # 按性别统计问卷数量
count_by_age = df.groupby('age').size()         # 按年龄统计问卷数量

# 数据可视化
count_by_gender.plot(kind='bar')
plt.title('Survey Responses by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

count_by_age.plot(kind='line')
plt.title('Survey Responses by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

 
    
