def bin_sort(li,min_num=0,max_num=99,bin_num=8):
    bin = [[] for i in range(bin_num)]

    for num in li:
        n = (max_num-min_num+1) / bin_num
        #i=1 - 8 号桶  [(i-1)*n,i*n)
        bin[int(num // n)].append(num)
        #维护桶有序
        li = bin[int(num // n)]
        i = len(bin[int(num // n)]) - 1
        temp = li[i]
        j = i - 1
        while j >= 0 and temp < li[j]:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = temp
    res = []
    print(bin)
    for l in bin:
        res.extend(l)
    return res

import random
li = [random.randint(0,99) for i in range(100)]
print(bin_sort(li))

