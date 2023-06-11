# 第十四周 Python笔记



2023-5-22 to 2023-5-28



# 一些笔记



excel文件的导入



\################### 导入Excel文件   ############################



import  pandas  as  pd



# 导入/读取excel文件，读取第一个sheet，同一文件夹中，无需写路径

# df是一个DataFrame

df=pd.read.excel('excel.xlsx',sheet*name='sheet1',index= , head=, )*



index*col=0  # 设置第零行为行索引*

header=0    # 设置第零列为列索引

head=None   # 不指定列索引



# 输出前五条数据

df1=df.head()



# 访问某列数据，并统计



# 解决"列对不齐"的问题

pd.set*option('display.unicode.east*asian*width',True)*



\#####################   读取数据    ##########################

# 用 数字索引 或 标签索引



df1=df.loc["明日"]     # 标签索引 loc以列名或行名来抽取

df1=df.iloc[0]        # 数字索引  iloc以行和列的位置索引来抽取



# 抽取指定列数据，用loc和iloc方法



print(df.loc[:,["语文","数学"]])



print(df.iloc[:,:2])    # 连续抽取从1列开始到第3列



# 去除空值



# 分组

df1=df1.groupby("一级分类").sum()

# 赵明月的笔记



# 14周 本周Python作业：



分析每一列数据，所以大概要写十几个程序，但这十几个程序是相似的



学会以下内容：



分组计数



合并



抽取



查看数据分布



去除空值



info



# GPT整理我的笔记：



以下是关于Python读取文件的知识点的整理笔记：



1.  

导入Excel文件：使用pandas库的read*excel函数来导入Excel文件。可以指定文件名、工作表名等参数来读取数据。例如：*

import  pandas  as  pd

df  =  pd.read*excel('excel.xlsx', sheet*name='sheet1')



2.  

设置行和列索引：通过设置index*col和header参数，可以指定哪些行或列作为索引。例如：*

index*col  =  0   # 将第零行作为行索引*

header  =  0      # 将第零列作为列索引

head  =  None     # 不指定列索引



3.  

输出数据：使用DataFrame的head()方法可以输出前几条数据。例如：

df1  =  df.head()



4.  

访问数据：使用loc和iloc方法可以通过标签索引或数字索引来访问数据。例如：

df1  =  df.loc["明日"]    # 标签索引，抽取"明日"这一行的数据

df1  =  df.iloc[0]       # 数字索引，抽取第一行的数据



5.  

抽取指定列数据：使用loc和iloc方法可以抽取指定的列数据。例如：

print(df.loc[:, ["语文", "数学"]])    # 抽取"语文"和"数学"这两列的数据

print(df.iloc[:, :2])               # 连续抽取从第一列到第三列的数据



6.  

处理空值：使用pandas的函数或方法来处理空值，例如fillna()方法可以填充空值，dropna()方法可以删除含有空值的行或列。



7.  

分组：使用groupby()方法可以对数据进行分组，常用于统计、聚合等操作。例如：

df1  =  df.groupby("一级分类").sum()   # 按"一级分类"列进行分组，并对其他列进行求和



这些是关于Python读取文件的一些基本知识点，可根据具体需求和情况进行进一步学习和应用。



就是引用



> 笔记类软件统称 引用



