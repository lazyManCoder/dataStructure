def sift(li,low,high):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= high:   
        #j 只想更大的数字
        if j + 1 <= high and li[j+1] > li[j]:
            j = j + 1  #如果右孩子存在并且更大，j指向右孩子
        if tmp < li[j]:
            li[i] = li[j]
            i = j 
            j = 2 * i + 1
        else:   #退出条件：tmp的值大于两个孩子的值
            break
    li[i] = tmp

def heap_sort(li):
    #建堆
    n = len(li)
    for i in range(n//2-1,-1,-1):
        #i 是建堆是要调整的子树的根和小标值
        sift(li,i,n-1)  #high在最后不影响结果
    #挨个出数
    for i in range(n-1,-1,-1): #i当前的high值
        li[i],li[0] = li[0],li[i]
        #现在堆的范围0- i-1
        sift(li,0,i-1)


import random
li = list(range(10))
random.shuffle(li)
print(li)
heap_sort(li)
print(li)




