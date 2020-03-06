def swapBit(x,i,j):
    if ((x>>i) & 1 and (x>>j) & 1):
        x ^= ((1<<i) | (1<<j))
    return x
x = 0b100100
i = 2
j = 3
a = swapBit(x,i,j)
print(a,bin(a))


