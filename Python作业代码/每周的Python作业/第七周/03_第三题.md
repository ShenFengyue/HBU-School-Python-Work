```Python
#这是第三题
 
#最开始写好了，然后找不到保存在哪里了。。。换了个方法又写了一遍。
 
# 输入一个正整数n
n = int(input("请输入一个正整数n: "))
 
# 定义一个变量，记录是否有满足条件的数
found = False
 
# 遍历从1到n的所有整数，如果满足条件，就输出，并把found设为True
for m in range(1, n + 1):
    if m % 3 == 2 and m % 5 == 3 and m % 7 == 2:
        print(m)
        found = True
 
# 如果没有任何一个数满足条件，就打印"No solution."
if not found:
    print("No solution.")
```
