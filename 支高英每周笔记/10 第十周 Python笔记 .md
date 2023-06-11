# 第十周 2023-4-23

**异常处理**

------

except ==TypeError==:

print("列表包含非数字元素")

print("不能输入浮点数")

except ==ZeroDivisionError==:

print("列表长度为0")

IndexError

输入的数值不在0-5之内

NameError

输入的不是数字

name x is not defined, 所以叫NameError

NameError和TypeError有啥区别？

ls=eval() 可生成列表

**文件处理**

------

**文件的打开与关闭**

可打开 txt，xlxs，csv

写入 write

读取 read

打开 open

关闭 close

**文件读取笔记**

filename用文件路径

下一级目录 \

上一级目录 ..

但是用\会产生问题，因为\n是换行，所以有以下三种解决方案：

/

\     （两个转义字符）

r+目录

**mode="r"**

r 只读模式

w 不读，创建空文件

a 不读，追加新数据，或创建空文件

r+ 能写，必须有文件

a+读不到内容，因为文件指针默认在最后一行

t 以文本模式打开

x 创建一个空的，若已存在，报错FileExistsError

encoding=None

指编码方式

ASCII 英文

gbk 中文

gb2312 中文

utf-8 各种语言

read 读取所有内容

readline 读取第一行

readlines 读取所有行  （返回以\n为分隔符的字符串列表）

"""

以下为一段真正可行的读取文件代码：

import time with open('D:/桌面/人生路线.txt', 'r', encoding='utf-8') as f:    t = f.readlines()    print(t) time.sleep(5)  # 暂停5秒钟

打开的txt文件，python将其作为==长字符串==

ROM 只读存储器

RAM

光标叫做文件指针，写入文件后，指针就会位于文件末尾

程序和被打开文件放在同一目录下，则读取时可以直接写文件名字

**Thoughts:**

------

已经学到了文件处理，老师也提到了网页信息抓取。

我又想起之前的遗传算法。

其实可以使用工具，来通过技术抓取一些网站的东西，然后进行分析。

？爬一下河北大学微博超话过去三四年的数据

**统计学Notes:**

------

通过Z分数，将任何一个正态分布转化为标准正态分布，然后±SD就是Z分数±1

正态分布表中的Z Y P分别是，Z分数，高度，概率。

