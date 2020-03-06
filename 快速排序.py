import time 
def cal_time(func):
    def inner(*args,**kwargs):
        time1 = time.time()
        func(*args,**kwargs)
        time2 = time.time()
        print('this is consume %s miao'%(time2-time1))
    return inner


def paration(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li,left,right):
    if left < right:
        mid = paration(li,left,right)
        _quick_sort(li,left,mid-1)
        _quick_sort(li,mid+1,right)

@cal_time
def quick_sort(li):
    return _quick_sort(li,0,len(li)-1)

li = list(range(10000,0,-1))
import random
random.shuffle(li)
quick_sort(li)
print(li)
