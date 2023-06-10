#----------------打开读写文件，并以字典组织存储数据--------------
import numpy as np
import matplotlib as mpl
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pandas as pd



excel_path = "data.xlsx" #excel文件路径
df = pd.DataFrame(pd.read_excel(excel_path)) #读取excel表格

#过滤掉空值
df1=df[df.iloc[:,-1].notnull()]

list1=df1.iloc[:,-1]

text_data = ''.join(list1) #链接字符串

print(text_data)

text=""
text += " ".join(jieba.cut(text_data))  # 将文本数据分词后存入text中

#-----------------绘制词云图-------------------
backgroud_Image = plt.imread(r"background.jpg")	# 设置词云背景


# -----------------设置词云样式-----------------
wc = WordCloud(
   
    background_color="yellow",			# 设置背景颜色
    
    mask=backgroud_Image,			# 设置背景图片
    font_path=r"C:\Windows\Fonts\SimHei.ttf",   # 设置中文字体
    max_words=100, 				# 设置最大现实的字数
    stopwords={"空","无"},			# 设置停用词
    max_font_size=50,				# 设置字体最大值
    random_state=100)				# 设置配色数

wc.generate_from_text(text)			# 生成词云
wc.recolor(color_func=ImageColorGenerator(backgroud_Image)) 

plt.figure(figsize=(10,10))    #创建自定义图像,大小为10*10英寸
plt.imshow(wc)					# 绘出词云图
plt.axis("on")					# 是否显示x轴、y轴下标


plt.show() 	
