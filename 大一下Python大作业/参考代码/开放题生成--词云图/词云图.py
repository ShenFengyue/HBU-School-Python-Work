#----------------打开读写文件，并以字典组织存储数据--------------
import numpy as np
import matplotlib as mpl
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


f=open('D:\桌面\Python\支高英大作业\参考代码\开放题生成--词云图\data.txt','r',encoding="utf-8")

t=[]
for cc in f:
    tc=cc.replace("\n","")  #tc是data.txt文件中的一行，去除每行末尾的"\n"
    t.append(tc)            #t是以文件中的一行为元素的列表
print(t)


#-----------以\t为分割字符生成二维列表Ls----------------
Ls=[]
for ts in t:
    ls=ts.split("\t")
    Ls.append(ls)
print(Ls)
#-----------以字符串数据结构组织数据，生成字符串text_data----------------
text_data=""
for d_cn in range(1,len(Ls)):
    
   text_data=text_data+Ls[d_cn][len(Ls[0])-1]
print(text_data)
f.close()


#-----------词云图数据---------
text=""
text += " ".join(jieba.cut(text_data))  # 将文本数据分词后存入text中

#-----------------绘制词云图-------------------
backgroud_Image = plt.imread(r"background.jpg")	# 设置词云背景


# -----------------设置词云样式-----------------
wc = WordCloud(
   
    background_color="yellow",			# 设置背景颜色
    
    mask=backgroud_Image,			# 设置背景图片
    font_path=r"C:\Windows\Fonts\SimHei.TTF",   # 设置中文字体
    max_words=100, 				# 设置最大现实的字数
    stopwords={"空","无"},			# 设置停用词
    max_font_size=50,				# 设置字体最大值
    random_state=100)				# 控制单词颜色的随机状态

wc.generate_from_text(text)			# 生成词云
wc.recolor(color_func=ImageColorGenerator(backgroud_Image)) #获得背景图的颜色值

plt.figure(figsize=(10,10))    #创建自定义图像,大小为10*10英寸
plt.imshow(wc)					# 绘出词云图
plt.axis("on")					# 是否显示x轴、y轴下标


plt.show() 					# 显示词云图


