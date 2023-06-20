# Python模拟题解析

选择题：
4、执行下方代码段后，输出结果是（  ）。
Li01 = [3, 1, 2, 5, 4]
Li01 = Li01.sort()
print(Li01)
正确答案：A： None
解析：列表的sort()方法在原地对列表进行排序，并且不返回任何结果。因此，Li01 = Li01.sort()将Li01赋值为None，所以打印Li01的结果是None。

9、执行下方代码后，描述正确的是（  ）。
li01 = [1, 2, 3, 4, 5]
li02 = li01
li02.append(6)
正确答案：A： li01中的数据为 [1, 2, 3, 4, 5, 6]，li02中的数据为 [1, 2, 3, 4, 5, 6]
解析：li01和li02引用同一个列表对象，所以对li02的操作也会影响li01。li02.append(6)会在li02末尾添加6，li01和li02都会变成[1, 2, 3, 4, 5, 6]。

11、执行代码print('9' > '10')的结果是（ ）。
正确答案：B： False
解析：字符串'9'的Unicode码值为57，而字符串'10'的Unicode码值为49，所以'9'不大于'10'，所以表达式'9' > '10'的结果为False。

13、执行代码 s = 'Hello\n世界' 后，len(s) 的值是（  ）。
正确答案：C： 10
解析：字符串s包含5个可见字符（'H', 'e', 'l', 'l', 'o'）和一个换行符（'\n'），以及两个中文字符（'世', '界'）。len(s)返回字符串s中的字符数量，所以结果为10。

15、(理工) 下列运算结果描述正确的是（  ）。
正确答案：D： 23<<2的结果是29
解析：位运算符<<表示左移操作，将一个数的二进制表示向左移动指定的位数。23的二进制表示为10111，左移2位后变成101110，对应的十进制数为29。

填空题：
1、1）对于元组 D = (0, 'ab', 'd', 3, 4)，len(D) 的结果是__(1)__. 答案：5
解析：元组D包含5个元素，len(D)返回元组D中元素的数量，所以结果为5。

2）已知 s = '秋处露秋寒霜降'，则语句 print(s[::-1]) 的结果是__(2)__. 答案：降霜寒秋露处秋
解析：s[::-1]表示从后向前取字符串s的所有字符，步长为-1，即逆序。所以结果为降霜寒秋露处秋。

3）print("{:05}".format(5))的结果是__(3).__。（书写答案时，请不要添加任何非必要的空格等空白字符）

解析：
"{:05}".format(5)表示将数字5格式化为5位数，不足5位的用0补齐。因为5本身只有一位，所以结果是00005。

代码实现：
```python
result = "00005"
```

2、1）Python 中 print(chr(97))的结果是__(1).__。（书写答案时，请不要添加任何非必要的空格等空白字符）

解析：
chr(97)表示将Unicode编码为97的字符转换为对应的字符，97对应的字符是小写字母'a'。

代码实现：
```python
result = "a"
```

2）语句 print(19-3**2+8%3) 的结果是__(2).__。（书写答案时，请不要添加任何非必要的空格等空白字符）

解析：
19-3**2+8%3的计算顺序为先进行指数运算，再进行乘法和取模运算，最后进行减法运算。3的平方是9，8除以3的余数是2。因此，表达式的结果是19-9+2=12。

代码实现：
```python
result = 12
```

1. Python中用于开启循环结构的两个关键字是：for和__(3).__。（书写答案时，请不要添加任何非必要的空格等空白字符）

解析：
Python中用于开启循环结构的两个关键字是for和while。

代码实现：
```python
result = "while"
```

综合应用题
1、编辑prog1.py文件，判断空气中二氧化碳状态（10分）
二氧化碳是空气中的化合物，程序接收用户输入的一个数值型数据，表示当前空气中二氧化碳的含量，该数据超过2000（即大于2000）输出“浓度偏高”，该数据不超过1000（即小于或等于1000），输出“正常”，数据介于1000到2000之间（即大于1000，小于或等于2000），输出“略高”
注1：输入使用input()，不要增加任何额外的提示信息

考生代码应写在如下两行注释之间

#Function-fun-start

#Function-fun-end

代码实现：
```python
#Function-fun-start
value = int(input())
if value > 2000:
    print("浓度偏高")
elif value <= 1000:
    print("正常")
else:
    print("略高")
#Function-fun-end
```

2、拍7游戏（10分）
编辑prog2.py文件，完成如下要求：

编写程序，接收用户通过键盘输入的一个正整数形式数据，输出从1开始到这个整数（

包含这个整数）间所有能被7整除或包含数字7的数字。每个数字输出占一行。
输入使用 input() ，不要附加任何参数和提示信息。

考生代码应写在如下两行注释之间

#Function-fun-start

#Function-fun-end

代码实现：
```python
#Function-fun-start
n = int(input())
for i in range(1, n+1):
    if i % 7 == 0 or '7' in str(i):
        print(i)
#Function-fun-end
```

3、苹果、橙、李子（15分）
编辑prog3.py文件，实现如下功能。
程序接收用户通过键盘输入的一个整数形式数据，假设该整数数值为 n。按1只苹果4元，1只橙子3元，4只李子1元，现在已有n元（n即键盘接收的整数形式数据数值），需要买n个果子（果子必须为整数个），一共可以买多少只苹果、多少只橙子、多少只李子？
注1：输入使用input()，不要增加任何额外的提示信息；
注2：输出数据时，按序输出苹果、橙子和李子的值，整数形式，数值间使用一个空格分隔；
注3：行与行顺序由每行的第一个数据，即苹果个数决定，由小到大顺序。

考生代码应写在如下两行注释之间

#Function-fun-start

#Function-fun-end

代码实现：
```python
#Function-fun-start
n = int(input())
for i in range(n//4 + 1):
    for j in range(n//3 + 1):
        k = n - 4*i - 3*j
        if k >= 0 and k % 1 == 0:
            print(i, j, k)
#Function-fun-end
```

4、自定义函数（15分）
编辑prog4.py文件，在指定位置，按要求编写程序，程序已有代码不要修改，也无需关注，考生只需在指定位置书写两个自定义函数即可，不要书写任何测试用代码。

考生代码应写在如下两行注释之间

#Function-fun-start

#Function-fun-end

代码实现：
```python
#Function-fun-start
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isFun(num):
    if not isPrime(num):
        return False
    digit_sum = num % 10 + num // 10 % 10
    if digit_sum % 10 == num // 100:
        return True
    return False
#Function-fun-end
```

5、IP地址判断（10分）
编辑prog5.py文件，实现如下功能：
程序依次接收20行用户通过键盘输入的数据，每行数据均为由三个英文点号

分开的4个整数数据，示例如下：
10.186.1.1
256.0.0.3
192.168.0.255
...（共20行）...

对于每行中的每个整数数据，值的范围应介于 0（含）到255（含）之间。因此，以上示例中 10.186.1.1 和 192.168.0.255 为两条合规数据，256.0.0.3 是一条非合规数据。
程序逐行判读数据是否合规，并统计合规和不合规的数目，最后按序分别输出合规和不合规数据的值（整数形式输出）。
程序最后输出的结果类似如下两行数据（2行数值相加应为20）：
18
2

### 四个数字都在0-255之间，就是合法的IP地址

考生代码应写在如下两行注释之间

#Function-fun-start

#Function-fun-end

代码实现：
```python
#Function-fun-start
valid_count = 0
invalid_count = 0

for _ in range(20):
    ip = input()
    nums = ip.split('.')
    valid = True
    for num in nums:
        if not num.isdigit() or not 0 <= int(num) <= 255:
            valid = False
            break
    if valid:
        valid_count += 1
    else:
        invalid_count += 1

print(valid_count)
print(invalid_count)
#Function-fun-end
```

6、文件操作（10分）
编辑prog6.py文件，实现如下功能：
打开文本文件 data6.txt ，文件内为若干行如下形式形式的文本：
3, 8, 9, 5, 7, 15, 6, 7
15 32 74 8 9
该文件可自行打开查看具体内容，此处共示意两行。
文件中每行数据均为用英文逗号或空格分开的数值，程序找出每行数据中的最大值，减去每行数据中的最小值，按序逐行存入一个名为 out6.txt 的文件中。按如上 data6.txt 文件示例，out6.txt 中的内容应为：
12
66

考生代码应写在如下两行注释之间

#Function-fun-start

#Function-fun-end

代码实现：
```python
#Function-fun-start
with open('data6.txt', 'r') as file:
    lines = file.readlines()

result = []
for line in lines:
    nums = line.strip().replace(',', ' ').split()
    nums = list(map(int, nums))
    result.append(max(nums) - min(nums))

with open('out6.txt', 'w') as file:
    for res in result:
        file.write(str(res) + '\n')
#Function-fun-end
```