'''
这破题，题目输入输出示例怎么和调试时自动输入的内容不一致啊，明明已经读取文件了，你还弄什么输入呢？谁出的这破题
'''
# 定义函数部分

# 定义函数getNewTime(t,m)，计算并返回调整后的时间
def getNewTime(t,m):
    # 将时间字符串转换为整数
    hour, minute, second = map(int, t.split(":"))
    # 计算总秒数
    total_seconds = hour * 3600 + minute * 60 + second
    # 加上增加的分钟数
    total_seconds += m * 60
    # 计算新的小时，分钟和秒数
    new_hour = (total_seconds // 3600) % 24
    new_minute = (total_seconds % 3600) // 60
    new_second = total_seconds % 60
    # 创建一个datetime对象
    new_time = datetime.datetime(1900, 1, 1, new_hour, new_minute, new_second)
    # 返回新的时间字符串，使用新的格式化方法
    return ' {new_time.hour}: {new_time.minute:02}: {new_time.second}'.format(new_time=new_time)

# 主程序部分

# 打开文件schedule.txt，并读取所有行
with open("schedule.txt", "r") as f:
    lines = f.readlines()
# 遍历每一行
for line in lines:
    # 去掉换行符
    line = line.strip()
    # 调用函数getNewTime(t,m)，传入原定时间和增加的分钟数（15）
    new_time = getNewTime(line, 15)
    # 打印原发车时间和新发车时间，用制表符分隔
    print(line + "\t" + new_time)
