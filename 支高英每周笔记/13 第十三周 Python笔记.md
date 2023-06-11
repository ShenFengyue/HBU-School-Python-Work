# 第十三周 Python笔记

# GPT整理笔记

# 第十三周 Python笔记

2023-5-15

## NumPy

NumPy是一个科学计算库，主要用于处理数组数据。它提供了强大的多维数组对象和相应的操作函数，是许多数据分析和科学计算任务的基础库。

### 导入NumPy库

要使用NumPy库，需要先安装它并导入：

```python
pip install numpy
import numpy as np
```

### 创建数组

NumPy中最基本的数据结构是数组（Array）。可以使用NumPy提供的函数创建数组。

#### 使用array创建数组

使用`np.array()`函数创建数组，可以传入一个序列（如列表或元组）作为参数，生成一个NumPy数组：

```python
data = np.array([[1, 2, 3], [4, 5, 6]])
```

#### 使用arange创建数组

使用`np.arange()`函数创建数组，可以生成一个等差数列：

```python
a = np.arange(start, stop, step)
```

#### 创建全零或全一数组

可以使用`np.zeros()`和`np.ones()`函数创建全零或全一的数组：

```python
zeros_array = np.zeros((2, 3))
ones_array = np.ones((2, 3))
```

#### 使用linspace创建数组

使用`np.linspace()`函数创建等差数列：

```python
linspace_array = np.linspace(start, stop, num)
```

#### 随机生成数组

可以使用`np.random.rand()`和`np.random.randint()`等函数随机生成数组。

### 数组切片与索引

可以使用切片和索引操作来访问和修改NumPy数组中的元素。

```python
# 3x3的二维数组，访问第1、2行和第2、3列的交叉部分
n[:2, 1:]

# 访问第2行和第1、2列的交叉位置
n[1, :2]

# 仅访问第一列
n[:, 1]
```

### NumPy基础运算

NumPy中的数组支持基本的数学运算。通过使用数组运算，可以对数组中的每个元素进行相同的操作。

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a * 3)  # 将数组中的数字变为3倍
```

## Pandas

Pandas是一个开源数据分析和处理工具，它提供了两种常用的数据结构：Series和DataFrame。

### Series

Series是带标签的一维同构数据结构，可以看作是一维数组或一列数据。它由两部分组成：索引（index）和数据（data）。索引提供了数据的标签，可以用来访问和操作数据。

可以通过传入列表、元组、字典或数组来创建Series对象，并指定索引：

```python
import pandas as pd

s1 = pd.Series([88, 60, 75], index=[1, 2, 3])
s2 = pd.Series([88, 68, 75], index

=["Chinese", "Math", "English"])

print(s1)
print(s2)
```

### DataFrame

DataFrame是带标签的、大小可变的、二维同构表格结构，可以看作是一个表格或一个电子表格。它由行索引（index）、列索引（columns）和数据（data）组成。

使用Pandas可以读取Excel文件，并将其转换为DataFrame对象，方便进行数据分析和处理。

```python
import pandas as pd

data = pd.read_excel('data.xlsx')
```

DataFrame可以从多个来源创建，例如传入列表、字典、数组等。

```python
import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
```

### 数字索引和标签索引

在Pandas中，可以使用数字索引和标签索引来访问DataFrame中的数据。需要注意的是，数字索引的终止值不包含在结果中，而标签索引的终止值是包含在结果中的。

以上是关于NumPy和Pandas的一些基本知识点和操作示例。希望对您有帮助。如有任何进一步的问题，请随时提问。











# 原笔记



2023-5-15

## numpy

科学计算库

可以处理数组

三维数组的秩是 3

### 创建数组

```pytho
pip install numpy
import numpy as np
```

### 创建数组 (1) array创建

da1=np.array((1,2,3),(4,5,6))

### shape计算数组多少行，多少列

print(data,shape)

print(dal)

\>\>\>[[1,2,3],

   [4,5,6]]# 创建数组 (2)

arange(start,stop,step)

a=np.array(0,1,0.1)

### 创建数组(3) Excel 其实就是个n行n列，全为0的二维数组

np,zeros((2,3))

array([[0,0,0]

      [0,0,0]])

np.ones()

### 创建数组(4) 创建一个一维数组，创建等差数列

np.linspaces()

np.random.rand(m,n)

np.random.randint(a,b)

**### 二维数组切片式索引**

`# 3*3的二维数组，访问第1，2行，和第2，3列的交叉部分`

n[:2,1:]

### 访问第2行，和第1，2列的交叉位置

n[1,:2]

### 仅仅访问第一列

n[:,1]

**### Numpy基础运算**

> number+python=Numpy	???
> [1,2,3,4,5]	列表
> [1 2 3 4 5]	数组

`# 将数组中的数字变为3倍`

import numpy as np

a=np.array([1,2,3,4,5])

print(a*3)*

**## Pandas**

Series	带标签的一维同构数据

> 开头的Series一定要大写！！！

DataFrame 带标签的，大小可变的，二维同构表格

标签：语文，数学，英语

用Pandas读取Excel，得出DataFrame

series	列表，元组，字典，数组

index设置行索引,有几个对象，就设置几个索引

`import pandas as pd`

s1=pd.Series([88,60,75],index=[1,2,3])

s2=pd.Series([88,68,75],index=("Chinese","Math","English"))

print(s1)

print(s2)

下载numpy，不小心下载到python3.8了，必须用这个解释器才行

Pandas

数字索引，终止值不包含

标签索引，包含



## 问题

series到底是什么？

C:UserslenovoAppDataRoamingPythonPython38

C:UserslenovoAppDataLocalProgramsPythonPython311

> 您好，这是Bing。根据我的搜索结果，cmd下载numpy时默认选择python3.8作为解释器的可能原因是：

-  \> 您的系统环境变量中，python3.8的路径优先级高于python3.11的路径¹²。
-  \> 您的pip命令没有指定使用python3.11的解释器，而是使用了默认的python3.8的解释器¹²。\> 您可以尝试以下方法来解决这个问题：

-  \> 修改系统环境变量，将python3.11的路径放在python3.8的路径之前¹²。
-  \> 使用py -3.11 -m pip install numpy命令来指定使用python3.11的解释器来安装numpy²。\> 希望这能帮助您。



