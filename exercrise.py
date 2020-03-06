def sift(li,low,high):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= high:
        if j+1 <= high and li[j+1] > li[j]:
            j = j+ 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break

    li[i] = tmp

def heap_sort(li):
    n = len(li)
    for i in range(n // 2-1,-1,-1):
        sift(li,i,n-1)

    for i in range(n-1,-1,-1):
        li[i],li[0] = li[0],li[i]
        sift(li,0,i-1)

import random
li = list(range(100))
random.shuffle(li)
heap_sort(li)
print(li)