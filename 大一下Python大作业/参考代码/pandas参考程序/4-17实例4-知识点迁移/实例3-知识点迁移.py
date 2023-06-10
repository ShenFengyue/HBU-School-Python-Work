# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:06:19 2022

@author: z'g'y
"""

import pandas as pd  #导入pandas模块
df=pd.read_excel('date1.xlsx')
#抽取数据
df1=df[['1.您的性别?','序号']]
df1=df1.groupby('1.您的性别?')['序号'].count()
print(df1)