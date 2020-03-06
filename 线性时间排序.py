from cal_time import cal_time

@cal_time
def count_sort(li,max_num=100):
    #创建新列表计数
    count = [ 0 for i in range(max_num+1)]
    for num in li:
        count[num] += 1
    li.clear()
    for i,t in enumerate(count):
        for j in range(t):
            li.append(i)

@cal_time
def sys_sort(li):
    li.sort()

import random
import copy
li = [random.randint(0,100) for i in range(1000000)]
li2 = copy.deepcopy(li)
count_sort(li)
sys_sort(li)


