#创建列表
 
lis_good = []
lis_bad = []
 
#收集数据
 
while True:
        n = eval(input())
        if n == -1:
            break
        elif n < 60:
            lis_bad.append(n)
        else:
            lis_good.append(n)
 
#计算及格和不及格成绩的平均值
            
if len(lis_good) > 0:
    total_good = sum(lis_good)
    avg_good = total_good / len(lis_good)
    print("及格成绩的平均值是：", avg_good)
 
if len(lis_bad) > 0:
    total_bad = sum(lis_bad)
    avg_bad = total_bad / len(lis_bad)
    print("不及格成绩的平均值是：", avg_bad)
 
