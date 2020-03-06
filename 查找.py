
#print(li.index(4))

#顺序查找  遍历数组

#二分查找  时间复杂度   logn 要求有序  有序数列
# 从有序列表的候选区data[0:n]开始，通过对反查找的值与候选的区中间值的比较，可以使候选区减少一半
#切片是n
import time
def cal_time(func):
    def innner(*args,**kwargs):
        time1 = time.time()
        res = func(*args,**kwargs)
        time2 = time.time()
        print("time : %s" %(time2 - time1))
        return res
    return innner

@cal_time
def binary_search(li,val):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] < val:
            low = mid + 1
        elif li[mid] > val:
            high = mid - 1
        else:
             return mid
    return None

@cal_time
def linear_search(li,val):
    try:
        return li.index(val)
    except:
        None
li = list(range(0,1000000,2))
binary_search(li,999999)
linear_search(li,999999)