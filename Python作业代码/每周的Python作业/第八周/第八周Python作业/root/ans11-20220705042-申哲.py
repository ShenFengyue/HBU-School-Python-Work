# 这是第一道题

def isNarcissus(num):
     val = False
     a=num//100 #百位数
     c=num//10-a*10 #十位数
     b=num-a*100-c*10 #个位数
     if (num == a**3+b**3+c**3):
          val = True
     return val

for n in range(100,1000):
     if (isNarcissus(n)):
          print("%d是一个水仙花数"%n)
