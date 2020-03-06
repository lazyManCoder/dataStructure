#递是通过一个函数在执行的过程中一次或多次调用其本身
#计算机的文件系统有一个递归结构，在该结构中，目录能够以任意深度嵌套在其他目录上，
#递归算法广泛运用在探索和管理这些系统
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(10))

#英式标尺
def draw_line(tick_length,tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ''+tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
    draw_line(major_length,'0')
    for j in range(1,1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))
draw_interval(5)

def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)
