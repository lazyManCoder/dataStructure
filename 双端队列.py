class Deque(object):
    '''双端对列'''
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        '''从列表的头部进行插入'''
        self.__list.insert(0,item)

    def add_rear(self,item):
        '''往队列尾部添加一个item元素'''
        self.__list.append(item)

    def pop_fornt(self):
        '''从队列中删除一个元素'''
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        '''判断队列是否为空'''
        return self.__list == []

    def size(self):
        '''返回队列的大小'''
        return len(self.__list)

if __name__ == '__main__':
    s = Deque()

