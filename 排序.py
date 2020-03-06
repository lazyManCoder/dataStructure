'''
python sort
'''
import random

def bubble_sort(li):
    n = len(li)
    for i in range(n - 1):    #i表示的趟数
        for j in range(0,n-i-1):  #下标的箭头
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]


def select_sort(li):
    n = len(li)
    for i in range(0,n-1):
        min_pas = i
        for j in range(i+1,n):
            if li[j] < li[min_pas]:
                min_pas = j
        if min_pas != i:
            li[min_pas],li[i] = li[i],li[min_pas]





def insert_sort(li):
    n = len(li)
    for i in range(1,n):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            print(j)
            j -= 1
        li[j+1] = tmp

li = list(range(10))
random.shuffle(li)
print(li)
insert_sort(li)
print(li)
