def swap(x,i,j):
	if ((x>>i) & 1) != ((x>>j) & 1):
		x ^= ((1<<i)) | (1<<j)
	return x

x = 0b100100
i = 2
j = 3
x = swap(x,i,j)
