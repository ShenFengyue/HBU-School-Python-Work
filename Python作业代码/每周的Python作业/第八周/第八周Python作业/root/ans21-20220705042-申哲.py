# 这是第三道题

def FindWanshu(lst):
    for num in range(1,1000):
        s = num
        for i in range(1,num):
            if num % i == 0:
                s = s - i
        if s == 0:
            lst.append(num)

lst = []
FindWanshu(lst)

txt = ""
for item in lst:
    txt += str(item)
    txt += ","
print(txt[:-1])      #如果只有一行输出的话，不太理解这个print的作用。
print("1~1000之间的完数共有{}个".format(len(lst)))

