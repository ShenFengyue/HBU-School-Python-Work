# 这是第四道题

def Search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            k = i  # target在列表中的索引
            return k
    return -1  # 未找到，返回-1

L = [5, 7, 13, 25, 32, 46, 54, 62, 78, 83, 88, 91, 99]  
find = int(input('请输入要查找的整数：'))
n = Search(L, find)
if n == -1:
    print("未找到")
else:
    print(f"{find} 是第 {n+1} 个元素")
