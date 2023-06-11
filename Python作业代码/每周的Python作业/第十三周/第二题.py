# 定义函数部分
def FindWanshu(lst):
    for num in range(1,1000):
        s = num
        for i in range(1,num):
            if num % i==0:
                s=s - i
        if s == 0:
            lst.append(num)

# 主函数部分
f=open("wanshu.txt","w")
lst=[]
FindWanshu(lst)  # 调用函数

txt=""
for item in lst:
    txt += str(item)
    txt += ","
f.write(txt[ :-1])
f.close
print("1~1000之间的完数共有%d个" % len(lst))

 


 

