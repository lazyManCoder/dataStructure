'''

n : 问题规模
a : 起始盘子
b : 路过盘子
c : 目标盒子

三个步奏：
   1.把n-1个圆盘从a经过c移动到b
   2.把第n个圆盘从a移动到c
   3.把n-1个小圆盘从b经过a到c

'''

def hano(n,a,b,c):
    if n > 0:
        hano(n-1,a,c,b)
        print('%s ---> %s'%(a,c))
        hano(n-1,b,a,c)

hano(4,'a','b','c')

