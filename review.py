def bubble_sort(li):
	n = len(li)
	for i in range(0,n-1):
		for j in range(n-i-1):
			if li[j] > li[j+1]:
				li[j],li[j+1] = li[j+1],li[j]
				
def select_sort(li):
	n = len(li)
	for i in range(0,n-1):
		min_index = i
		for j in range(i+1,n):
			if li[j] < li[min_index]:
				min_index = j
		if min_index != i:
			li[min_index],li[i] = li[i],li[min_index]
			
def insert_sort(li):
	n = len(li)
	for i in range(1,n):
		tmp = li[i]   #给过来的牌
		j = i - 1
		while j >= 0 and li[j] > tmp:
			li[j+1] = li[j]
			j -= 1
		li[j+1] = tmp
			
def sift(li,low,high):
	tmp = li[low]
	i = low
	j = 2 * i + 1
	while j + 1 <= high:
		if j + 1 <= high and li[j+1] > li[j]:
			j = j + 1
		while tmp < li[j]:
			li[i] = li[j]
			i = j
			j = 2 * i + 1
		else:
			li[i] = tmp
	li[i] = tmp

def heap_sort(li):
	n = len(li)
	#建堆
	for i in range(n//2-1,-1,-1):
		#i 建堆时要调整的子树的根的下标
		sift(li,i,n-1)
	for i in range(n-1,-1,-1):
		#i 当前的high值 也表示棋子的位置
		li[i],li[0] = li[0],li[i]
		#现在堆的范围 0 - i-1
		sift(li,0,i-1)
		
		
	
	

import random
li = list(range(100))
random.shuffle(li)
print(li)
heap_sort(li)
print(li)