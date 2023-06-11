# 第九周 2023-4-17

“虽然你们不是专业弄这个（计算机专业）的，但我希望你们能用python去做一些专业的事情。”    ——支高英

\# 调用函数的四种方法 function() b=function() print(function()) if function():

参数传递有哪几种方式？

format六字口诀：添对宽，分精类

**用一个标准的定义函数求最大公约数题，展现在python中使用占位符：**

\# 如何在python中使用占位符 # 这是第二道题 # 穷举法求两数的最大公约数，最大公约数不会超过两数中的较小值 def hcf(u,v):    if u>v:        m=v    else:        m=u    for i in range(m,0,-1):   # 此处必须是从m遍历到0，因为两个质数的最大公约数是1        if (u%i==0) and (v%i==0):            return i     u=int(input("请输入第一个整数：")) v=int(input("请输入第二个整数：")) h=hcf(u,v)                                      # 按照地址传递参数 print("%d和%d的最大公约数为：%d"%(u,v,h))

用穷举法写个鸡兔同笼问题

break continue return 都可以使for循环提前结束

index用法：

lis=[] target=input() for i in lis:    if i=target:    k=lis.index(target)   #k是target在列表lis中的位置    return k

**Python中的异常处理**

------

比如说逻辑错误

\# 除数为0的情况 ls=eval(input()) s=0 for num in ls:    s=s+num avg=s/len(ls) """ 错误之处：ls如果是空列表，那就不能作为被除数 """

开发者要提前进行异常处理，并留一些端口，以便增加后续功能

python有哪些常见异常类型？

