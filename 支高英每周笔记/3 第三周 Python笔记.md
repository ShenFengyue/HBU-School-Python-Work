# 第三周 python笔记

2023-3-6

【2023年3月6日】

\## 字典

 

·

元组效率高，但只可读不可存

列表效率低，但可读可存

 

·

只有一个元素的元组，要在元素之后加逗号，否则不是元组了，是整型

例：  tu5=(36,)

 

·

i^2 forI in range(10,30,5):  #推导式创建列表

会输出 100,225,······

 

·

sorted(元组)=列表

sorted(字典)=列表

sorted(组合数据类型)=列表

 

·

元组里面套元组，或者列表里面套列表，就叫“二维元祖”和“二维列表”，索引时用[5][3]即可

 

·#{字典}

 

创建字典：

赋值法 dict={"数学":78,"语文":146,"英语":139}

函数法 dic5={[],[],[]}

推导式法 dic6={i:i*I for I in range(1,10,2)}

 

访问字典：

dic1[item] 访问每个键所对应的值

 

keys() 以???的形式返回所有键

values() 以???的形式返回所有值

items() 以???的形式返回所有键值对

 

用法：dict4.keys()

 

·

一些函数：

get

 

dic.get(k,v)

返回k对应的值，若无k，就返回v

 

setdefault

 

字典名.setdefault(k.v)

若k存在，就返回

若k不存在，就增加一个键值对，并返回v

 

update

 

dic1.update(dic2)

将dic中的键值对更新到dic1中

补充没有的，更新已有的

 

可用于字典的合并

 

更常用的更新方法：

dic{["数学"]}=97

 

·

删除字典元素

del 字典名[键]

 

字典名.pop(键，默认值)

存在，就删了键和键值对，不存在，就返回默认值

 

删除字典：

del 字典名

 

 

 

\# 有返回值的函数

pop

sorted

reverse 不输出数据类型

 

pop

popitem

get

update

setdefault

 

 

 

·#·

L=list(dic1.values())

total=sum(L) #求列表数据和

ave=total/len(L) #求列表中数据个数

 

 

 

 

 

 

 