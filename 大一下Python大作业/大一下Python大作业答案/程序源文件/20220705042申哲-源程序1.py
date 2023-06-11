import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('D:\桌面\Python大作业\data.xlsx')

# 指定要制作词云图的列名
column_name = '11、短视频对您有什么益处和害处'

# 提取数据并处理空数据
text_data = ""
for row in df[column_name]:
    if pd.notnull(row) and row != "(空)" and "无" not in str(row) and "的" not in str(row):
        text_data += str(row)

# 文本分词
text = " ".join(jieba.cut(text_data))

# 创建词云图对象
wc = WordCloud(
    background_color="white",
    max_words=100,
    font_path="C:\Windows\Fonts\SimHei.TTF"
)

# 生成词云图
wc.generate_from_text(text)

# 显示词云图
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
